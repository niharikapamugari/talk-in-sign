"""Upload Talk in Sign's local BridgeConn clips to a public Hugging Face dataset.

Usage (PowerShell):
  $env:HF_TOKEN = "hf_your_write_token"
  py scripts/upload_sign_videos_to_huggingface.py --repo YOUR_USERNAME/talk-in-sign-isl-videos

Never commit or share the token. The upload is resumable: run the same command
again if the connection is interrupted.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLIPS_DIR = ROOT / "frontend" / "public" / "assets" / "signs"
CARD_PATH = Path(__file__).with_name("huggingface-sign-videos-README.md")


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish local ISL MP4 clips to Hugging Face.")
    parser.add_argument("--repo", required=True, help="Dataset repo, for example USERNAME/talk-in-sign-isl-videos")
    args = parser.parse_args()

    token = os.environ.get("HF_TOKEN")
    if not token:
        print("HF_TOKEN is missing. Create a Hugging Face write token and set it only in this terminal session.")
        return 2
    if not CLIPS_DIR.is_dir() or not any(CLIPS_DIR.glob("*.mp4")):
        print(f"No MP4 clips found in {CLIPS_DIR}")
        return 2

    try:
        from huggingface_hub import HfApi
    except ImportError:
        print("Install the uploader first: py -m pip install --upgrade huggingface_hub[hf_xet]")
        return 2

    api = HfApi(token=token)
    api.create_repo(args.repo, repo_type="dataset", private=False, exist_ok=True)
    api.upload_file(
        path_or_fileobj=str(CARD_PATH),
        path_in_repo="README.md",
        repo_id=args.repo,
        repo_type="dataset",
        commit_message="Add Talk in Sign dataset card and attribution",
    )
    print("Uploading clips. This can take a long time; rerun the same command to resume if needed.")
    api.upload_folder(
        folder_path=str(CLIPS_DIR),
        path_in_repo="signs",
        repo_id=args.repo,
        repo_type="dataset",
        allow_patterns="*.mp4",
        commit_message="Upload licensed ISL sign videos",
    )
    print(f"Upload complete: https://huggingface.co/datasets/{args.repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
