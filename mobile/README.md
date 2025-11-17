React Native mobile skeleton. Features:
- Text prompt trigger (button/long-press)
- Voice wake-word (integrate Porcupine or Vosk for offline)
- Offline STT fallback (Vosk native integration)
- Push notifications via Firebase Cloud Messaging (FCM)

Instructions:
1. Clone mobile folder.
2. `npm install` (or `yarn`)
3. Configure API endpoint in App.js to your Cloud Run URL.
4. Integrate Porcupine/CMUSphinx/Vosk for wake-word and offline STT (native modules required).
5. Configure FCM keys and register device tokens to backend (not covered in this skeleton; see notes).
