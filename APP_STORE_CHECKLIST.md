# FairwayConnect → App Store checklist

Everything below is in order. Items marked **[YOU]** need your Apple ID, payment, or
a signup decision — they can't be done for you. Items marked **[DONE]** are already
in this repo. Anything else, ask Claude to do once the prerequisites exist.

## Phase 1 — Get the backend on the internet

The iOS app needs an API it can reach from anywhere.

1. **[YOU]** Pick a host and create an account. Easiest options (all have free tiers):
   - https://render.com — create a "Web Service" from this repo, start command `python3 server.py`, add a persistent disk mounted where `fairway.db` lives
   - https://railway.app or https://fly.io — same idea
2. Deploy. Verify `https://<your-app>.onrender.com` serves the app and you can sign in.
3. In `public/index.html`, add before the `app.js` script tag (only needed for the
   iOS build, the web app keeps using same-origin):
   ```html
   <script>window.FC_API_BASE = "https://<your-app>.onrender.com";</script>
   ```
4. Lock down CORS in `server.py` (replace `*` with your domains).

**Cheap validation shortcut:** the deployed URL already works as a PWA — on an
iPhone, open it in Safari → Share → "Add to Home Screen". Full-screen app, your
icon, no Apple approval. Share it with golf buddies before spending $99.

## Phase 2 — Apple accounts & tools

5. **[YOU]** Enroll in the Apple Developer Program ($99/yr): https://developer.apple.com/programs/enroll/
   — individual enrollment, takes ~24–48h to approve.
6. **[YOU]** Install full Xcode from the Mac App Store (~40 GB, needs your Apple ID).
   Then run: `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
7. **[YOU]** Install Homebrew (https://brew.sh), then: `brew install node cocoapods`

## Phase 3 — Build the iOS app (Claude can do all of this once Phase 2 is done)

8. In this folder:
   ```bash
   npm init -y
   npm install @capacitor/core @capacitor/cli @capacitor/ios
   npx cap add ios          # capacitor.config.json is already set up
   npx cap sync
   npx cap open ios         # opens Xcode
   ```
9. In Xcode: set your Team (Signing & Capabilities), set the app icon
   (`public/icons/icon-1024.png` is App Store size), bump the bundle ID if
   `com.fairwayconnect.app` is taken.
10. Run on the Simulator, then on a real iPhone.
11. Recommended before submitting (helps pass guideline 4.2 "minimum functionality"):
    - Add `@capacitor/push-notifications` for invite/message alerts
    - Add `@capacitor/camera` so posts can include round photos

## Phase 4 — App Store Connect

12. **[YOU]** Create the app record at https://appstoreconnect.apple.com:
    name **FairwayConnect** (have a backup name ready), bundle ID from step 9,
    category Social Networking.
13. Prepare the listing (Claude can draft all the text):
    - Screenshots: 6.7" and 6.5" iPhone sizes (take them in the Simulator)
    - Description, keywords, support URL
    - **Privacy policy URL** — required. A simple page stating what's collected
      (email, name, golf stats, posts) and how it's used. Host it anywhere.
    - Privacy "nutrition label" questionnaire: you collect Contact Info (email),
      User Content (posts, messages), Identifiers (user ID)
    - Age rating questionnaire (UGC questions → likely 12+ or 17+)
14. **EULA / UGC compliance** (guideline 1.2) — already implemented in the app:
    report posts ✓, block users ✓, delete own content ✓. In App Review notes,
    state how reports are handled (you review the `reports` table and remove
    offending content within 24h — and actually do this).
15. Archive in Xcode (Product → Archive) → upload to App Store Connect.
16. **TestFlight first**: invite yourself + friends, shake out bugs for a week.
17. Submit for review. Provide a **demo account** in the review notes
    (use a demo login, e.g. maria@demo.fairwayconnect.app / golf1234, on your
    deployed server). First review: 1–3 days. A first-try rejection is normal —
    fix what they cite and resubmit.

## Ongoing obligations

- Actually moderate: check the `reports` table regularly
  (`sqlite3 fairway.db "SELECT * FROM reports"`)
- Keep the $99/yr membership active or the app is delisted
- Respond to App Review inquiries within their deadlines
