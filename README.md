# FairwayConnect ⛳

The professional network for golfers — LinkedIn, but your handicap is your job title.

## What's here

| Path | What it is |
|---|---|
| `server.py` | Complete backend: REST API + static file server. **Zero dependencies** — Python 3 stdlib + SQLite only. |
| `public/` | The web app (vanilla JS SPA) + PWA manifest, service worker, icons. |
| `fairway.db` | SQLite database. Created and seeded with demo golfers on first run. Delete it to reset. |
| `make_icons.py` | Regenerates the app icons (requires Pillow). |
| `capacitor.config.json` | iOS wrapper config for the App Store build (see APP_STORE_CHECKLIST.md). |

## Run it

```bash
python3 server.py        # http://localhost:4173  (or PORT=8080 python3 server.py)
```

Sign in with a demo account (`maria@demo.fairwayconnect.app` / `golf1234` — see the
sign-in screen for the full list) or create your own.

## Features

- **Accounts** — signup/login, PBKDF2-hashed passwords, server-side sessions
- **Feed** — posts with optional scorecards (score/fairways/putts), "Nice shot" reactions, comments
- **My Foursome** — connection invites, accept/ignore, suggestions
- **Tee Times** — post open spots, request to join, spots tracked
- **Messaging** — threads with unread badges (light polling while the page is open)
- **Notifications** — invites, accepts, comments, endorsements, tee-time requests
- **Profiles** — handicap, rounds, best round, golf experience, endorsable strengths, courses played
- **Moderation (App Store guideline 1.2)** — report any post, block any user (mutual invisibility), delete your own posts

## Deploying the backend

Any host that runs Python works. The server binds `0.0.0.0` and respects `PORT`:

- **Render / Railway / Fly.io**: start command `python3 server.py`. Add a persistent
  volume for `fairway.db` or the database resets on each deploy.
- The frontend calls the API on the same origin by default. To point a separately
  hosted frontend (or the iOS app) at the API, set `window.FC_API_BASE = "https://your-api.example.com"`
  in a script tag before `app.js` loads.

## Before real users (hardening TODO)

- Serve over HTTPS (any of the hosts above do this for you)
- Lock CORS down from `*` to your app's origins (`Access-Control-Allow-Origin` in `server.py`)
- Add rate limiting on `/api/login` and `/api/signup`
- Session expiry (sessions currently live until logout)
- Email verification + password reset (needs an email provider, e.g. Resend/Postmark)
- Swap SQLite for Postgres if you outgrow a single server (the SQL is vanilla; this is a small change)

## App Store

See [APP_STORE_CHECKLIST.md](APP_STORE_CHECKLIST.md) for the complete path from here
to a listed iOS app, including the parts only you can do (Apple Developer enrollment).
