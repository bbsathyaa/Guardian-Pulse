Wake-word & offline STT integration notes
- Android: integrate Vosk via https://github.com/alphacep/vosk-android-demo or Picovoice Porcupine native.
- iOS: integrate Vosk iOS or Porcupine. Both require bundling small models.
- Use native modules to expose wake-word events to RN and to run offline STT.
- For Push notifications: configure Firebase Cloud Messaging -> get FCM token -> POST to backend /register_token endpoint to receive push alerts (when escalation occurs).
