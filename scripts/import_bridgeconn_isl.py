"""Download BridgeConn CC BY-SA 4.0 ISL clips and build the app manifest.

Only MP4 media plus metadata are retained; pose-estimation files are deliberately skipped.
Run from repository root:
  python scripts/import_bridgeconn_isl.py
"""
import io
import json
import re
import sys
import tarfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "frontend" / "public" / "assets" / "signs"
BACKEND_SRC_MANIFEST = ROOT / "backend" / "src" / "main" / "resources" / "sign-dictionary.json"
BACKEND_TARGET_MANIFEST = ROOT / "backend" / "target" / "classes" / "sign-dictionary.json"

BASE_URL = "https://huggingface.co/datasets/bridgeconn/sign-dictionary-isl/resolve/main"

ALL_SHARDS = [
    "shard_00001-train.tar",
    "shard_00002-train.tar",
    "shard_00003-train.tar",
    "shard_00004-train.tar",
    "shard_00005-train.tar",
    "shard_00006-train.tar",
    "shard_00007-train.tar",
]

def clean(value):
    return re.sub(r"[^a-z0-9 ]", "", str(value).lower()).strip()

def strings(value):
    if isinstance(value, str): return [value]
    if isinstance(value, list): return [item for entry in value for item in strings(entry)]
    if isinstance(value, dict): return [item for entry in value.values() for item in strings(entry)]
    return []

def write_sample(key, sample, signs, terms):
    if "json" not in sample or "mp4" not in sample: return
    try: metadata = json.loads(sample["json"].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError): return
    glosses = strings(metadata.get("glosses", []))
    if not glosses:
        # Current BridgeConn shards store the English dictionary label here.
        glosses = strings(metadata.get("transcript", {}).get("text", ""))
    if not glosses: return
    gloss = re.sub(r"\s+", "_", clean(glosses[0]).upper())
    if not gloss: return
    file_name = re.sub(r"[^A-Za-z0-9_-]", "_", key) + ".mp4"
    dest_path = OUTPUT / file_name
    if not dest_path.exists():
        dest_path.write_bytes(sample["mp4"])
    video_url = "/assets/signs/" + file_name
    signs.setdefault(gloss, {"videoUrl": video_url, "terms": []})
    for term in glosses + strings(metadata.get("transcripts", [])):
        normalized = clean(term)
        if normalized and len(normalized.split()) <= 6:
            terms.setdefault(normalized, gloss)
            if normalized not in signs[gloss]["terms"]:
                signs[gloss]["terms"].append(normalized)

def expand_terms(signs, terms):
    # Expand numbered variants, compound words, and common synonyms
    for gloss, info in list(signs.items()):
        v_url = info.get("videoUrl")
        m = re.match(r"^(.+)_(\d+)$", gloss)
        if m:
            base_gloss = m.group(1)
            signs.setdefault(base_gloss, {"videoUrl": v_url, "terms": [clean(base_gloss.replace('_', ' '))]})
            base_term = clean(base_gloss.replace('_', ' '))
            if base_term: terms.setdefault(base_term, base_gloss)
            for t in info.get("terms", []):
                ct = clean(re.sub(r"\s*\d+$", "", t))
                if ct: terms.setdefault(ct, base_gloss)
        if "_" in gloss and not m:
            for part in gloss.split("_"):
                if len(part) >= 2 and not part.isdigit():
                    signs.setdefault(part, {"videoUrl": v_url, "terms": [clean(part)]})
                    ct = clean(part)
                    if ct: terms.setdefault(ct, part)

    if "FIND" not in signs and ("SEARCH_2" in signs or "FOUND" in signs):
        target = "SEARCH_2" if "SEARCH_2" in signs else "FOUND"
        signs["FIND"] = {"videoUrl": signs[target]["videoUrl"], "terms": ["find", "search"]}
    if "ME" not in signs and "I_ME" in signs:
        signs["ME"] = {"videoUrl": signs["I_ME"]["videoUrl"], "terms": ["me", "i"]}

    synonyms = {
        "help": "HELP", "water": "WATER", "drink": "DRINK", "drinking": "DRINK",
        "find": "FIND", "search": "SEARCH",
        "home": "HOME", "house": "HOUSE", "me": "ME", "i": "ME",
        "good": "GOOD", "day": "DAY", "need": "NEED", "duty": "DUTY",
        "eat": "EAT", "food": "FOOD", "go": "GO",
    }
    for term, g in synonyms.items():
        if g in signs: terms.setdefault(term, g)

def save_manifest(signs, terms, imported_shards):
    expand_terms(signs, terms)
    manifest = {
        "source": "BridgeConn Sign Dictionary ISL dataset",
        "sourceUrl": "https://huggingface.co/datasets/bridgeconn/sign-dictionary-isl",
        "license": "CC BY-SA 4.0",
        "attribution": "Sign videos: BridgeConn, Sign Dictionary ISL dataset, CC BY-SA 4.0.",
        "importedShards": sorted(list(imported_shards)),
        "signs": signs,
        "terms": terms,
    }
    text = json.dumps(manifest, ensure_ascii=False, indent=2)
    (OUTPUT / "manifest.json").write_text(text, encoding="utf-8")
    BACKEND_SRC_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    BACKEND_SRC_MANIFEST.write_text(text, encoding="utf-8")
    if BACKEND_TARGET_MANIFEST.parent.exists():
        BACKEND_TARGET_MANIFEST.write_text(text, encoding="utf-8")
    print(f"Manifest saved: {len(signs)} signs and {len(terms)} searchable terms.", flush=True)

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifest_path = OUTPUT / "manifest.json"
    signs, terms = {}, {}
    imported_shards = set()

    if manifest_path.exists():
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
            signs = existing.get("signs", {})
            terms = existing.get("terms", {})
            imported_shards = set(existing.get("importedShards", []))
            # If importedShards wasn't stored previously, mark shards 1 and 2 as already imported
            if not imported_shards and len(signs) > 500:
                imported_shards.add("shard_00001-train.tar")
                imported_shards.add("shard_00002-train.tar")
            print(f"Loaded existing manifest with {len(signs)} signs. Already imported: {sorted(imported_shards)}", flush=True)
        except Exception as e:
            print(f"Could not load existing manifest: {e}", flush=True)

    remaining_shards = [s for s in ALL_SHARDS if s not in imported_shards]
    if not remaining_shards:
        print("All 7 shards are already imported! Nothing to download.", flush=True)
        return

    print(f"Starting import of remaining {len(remaining_shards)} shard(s): {remaining_shards}", flush=True)

    for idx, shard_name in enumerate(remaining_shards, start=1):
        url = f"{BASE_URL}/{shard_name}"
        print(f"\n[{idx}/{len(remaining_shards)}] Downloading and extracting {shard_name}...", flush=True)
        samples = {}
        processed_count = 0

        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ISL-Translator-Importer/1.0"}
        )

        try:
            with urllib.request.urlopen(req, timeout=120) as response, tarfile.open(fileobj=response, mode="r|*") as archive:
                for member in archive:
                    if not member.isfile() or not (member.name.endswith(".json") or member.name.endswith(".mp4")):
                        continue
                    key, extension = member.name.rsplit(".", 1)
                    data = archive.extractfile(member).read()
                    sample = samples.setdefault(key, {})
                    sample[extension] = data
                    if "json" in sample and "mp4" in sample:
                        write_sample(key, sample, signs, terms)
                        del samples[key]
                        processed_count += 1
                        if processed_count % 100 == 0:
                            print(f"  Processed {processed_count} signs from {shard_name}...", flush=True)

            imported_shards.add(shard_name)
            print(f"Completed {shard_name}: {processed_count} signs processed.", flush=True)
            save_manifest(signs, terms, imported_shards)

        except Exception as err:
            print(f"Error importing {shard_name}: {err}", flush=True)
            save_manifest(signs, terms, imported_shards)
            raise

    print(f"\nALL 7 SHARDS SUCCESSFULLY IMPORTED! Total signs: {len(signs)}, Total terms: {len(terms)}.", flush=True)

if __name__ == "__main__":
    main()
