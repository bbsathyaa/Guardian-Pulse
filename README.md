Guardian-Pulse 🚨
A multimodal emergency-response agent with real-time dispatching, offline fallback, and encrypted incident logging.

Guardian-Pulse is an intelligent safety assistant designed to detect emergencies through text, voice wake-word, and multimodal inputs, and instantly connect the user to the nearest responder (police / ambulance) using OpenStreetMap, government emergency APIs (108), and multi-channel alerting (SMS, WhatsApp, Push).

Built with Google Cloud Run, Cloud SQL, Vertex AI, and secure encrypted logging, the system ensures that help is dispatched fast — even during offline or low-connectivity situations.

🚧 Features
🔊 Multimodal Emergency Activation

Text prompt activation

Voice wake-word trigger

Designed for low-latency detection

Optional silent-trigger for covert emergencies

🏥 Responder Routing

Finds nearest police station / ambulance / hospital via:

OpenStreetMap (OSM) geospatial lookup

Govt. Emergency API (108) fallback

Offline fallback → locally cached maps + nearest GPS cell lookup

📡 Dispatching & Notifications

Multi-channel alert delivery:

SMS (Twilio)

WhatsApp Alerts

FCM Push Notifications

Sends:

Live GPS

Photo/video evidence (optional)

Medical details (optional)

Device ID + timestamp

☁️ Backend Architecture

Cloud Run microservices

Cloud SQL (PostgreSQL) for user + incident storage

Vertex AI for intent detection:

Emergency vs non-emergency

Harm intent classification

Severity prediction

Cloud Tasks for automatic escalation:

Retries responders

Notifies backup services

Triggers extra monitoring

🔐 Security & Privacy

End-to-end encrypted incident logs

Location + medical data encrypted at rest

Zero-trust backend authorization

Emergency-only data retention

👥 Emergency Contact Escalation

Supports up to 3 trusted contacts

Automatic escalation if responders do not acknowledge

Contacts receive:

Live location

SOS type

Audio transcript (optional)

🧱 System Architecture Overview
User Trigger
  ├── Text / Voice Wake Word / App UI
  │
  ▼
Vertex AI Intent Classifier
  ├── Emergency Likely?
  ▼
Cloud Run Backend
  ├── Fetch nearest responder (OSM + Govt API)
  ├── Log encrypted incident
  ├── Dispatch tasks → SMS / WhatsApp / Push
  ▼
Cloud Tasks (Escalation)
  ├── Retry routines
  └── Notify emergency contacts (up to 3)

📂 Repository Structure
Guardian-Pulse/
│
├── /backend/        # Cloud Run services (Python/Node)
├── /frontend/       # Client app or web dashboard
├── /ml/             # Vertex AI prompt & training configs
├── /database/       # Migrations, schemas (Postgres)
├── /osm/            # Geo-lookup utilities + offline cache tools
└── README.md


(Adjust based on your actual folder structure—just tell me if you want it customized.)

🚀 Deployment
1. Set Environment Variables
GOOGLE_PROJECT_ID=
DATABASE_URL=
TWILIO_AUTH_TOKEN=
TWILIO_SID=
FCM_KEY=
WHATSAPP_API_KEY=
ENCRYPTION_SECRET=

2. Deploy Backend to Cloud Run
gcloud run deploy guardian-backend \
  --source backend \
  --region us-central1 \
  --allow-unauthenticated

3. Set Up Cloud SQL (PostgreSQL)
gcloud sql instances create guardian-db --database-version=POSTGRES_15
gcloud sql databases create guardian --instance guardian-db

4. Enable Vertex AI
gcloud services enable aiplatform.googleapis.com

🧪 Testing

Simulate voice wake-word locally

Run offline geolocation fallback tests

Trigger dummy incident → verify SMS + WhatsApp + Push delivery

Validate escalation workflow via Cloud Tasks

📜 License

MIT License — free to modify, distribute, and deploy.

🤝 Contributing

Pull requests and feature improvements are welcome.
Create an issue if you'd like to add:

Background audio detection

End-to-end encrypted media uploads

WearOS / smartwatch integration

✨ Authors

Guardian-Pulse Team
Maintained by: @bbsathyaa
