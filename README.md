# Talk in Sign

A full-stack, authenticated Text/Speech-to-ISL gloss translator. The current translation engine is deliberately rule and phrase based—not represented as an AI model—and is isolated behind `TranslationService` for future NLP/AI integration.

## Start

1. Create PostgreSQL database: `CREATE DATABASE isl_translator;`
2. Copy `backend/.env.example` values into environment variables (PowerShell: `$env:DB_PASSWORD="..."`). Set a strong `JWT_SECRET` outside local development.
3. Run backend: `cd backend; .\mvnw.cmd spring-boot:run`
4. Copy `frontend/.env.example` to `frontend/.env`, then run: `cd frontend; npm install; npm run dev`

The frontend defaults to `http://localhost:5173`; change `CORS_ALLOWED_ORIGIN` if needed. JPA creates/updates development tables without deleting data.

### Optional Groq AI simplification

Set `GROQ_API_KEY` before starting the backend to enable a server-side Groq step. It simplifies a sentence into concise English before the local, verified sign dictionary maps it to glosses. If the key is absent, the request fails, or a quota is exceeded, the rule-based translator continues automatically. The API key is never sent to the browser.

### Sign assets

Mapped glosses currently show an explicit “verified image or video not added yet” state. To add real media, update each sign entry's `imageUrl` or `videoUrl` in the backend dictionary only with licensed, verified ISL content. The UI supports both image and video URL fields without changing the API contract.

#### Included ISL video source

When `scripts/import_bridgeconn_isl.py` has been run, the application uses clips from **BridgeConn, Sign Dictionary ISL dataset** under the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/). The importer retains only MP4 clips and metadata, skips pose-estimation files, and creates the local video manifest used by the application. Any redistributed clips or adaptations must retain appropriate attribution and the same license.

## API

| Method | Endpoint | Auth |
|---|---|---|
| POST | `/api/auth/register` | No |
| POST | `/api/auth/login` | No |
| GET | `/api/auth/me` | Bearer JWT |
| POST | `/api/translation/text` | Bearer JWT |
| GET | `/api/translation/history?page=0&size=20` | Bearer JWT |
| DELETE | `/api/translation/history/{id}` | Bearer JWT |

For translation, post `{"text":"Hello, how are you?","inputType":"TEXT"}`. Speech uses the browser Web Speech API and submits its reviewed transcript as `SPEECH`.

## Notes

The sign dictionary provides verified gloss mappings for a limited common vocabulary and identifies unmapped words. No external video/image URLs or fabricated media assets are used. Add real ISL assets through a future dictionary/asset provider without changing the translation API.
