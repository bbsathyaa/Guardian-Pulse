1. Create GCP project and enable APIs: Cloud Run, Cloud SQL Admin, Secret Manager, Cloud Tasks, Cloud Scheduler, Vertex AI (optional).
2. Create a Cloud SQL Postgres instance (choose asia-south1 zone for India). Create DB and user.
3. Create Secret Manager secrets: TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM, EMERGENCY_CONTACTS_JSON (JSON array of up to 3 contacts), HMAC_KEY, FERNET_KEY, DB_PASS, BACKUP_CONTACTS_JSON.
4. Create service account for Cloud Run with roles: Cloud SQL Client, Secret Manager Secret Accessor, Cloud Tasks Enqueuer, Cloud Run Invoker.
5. Create Cloud Tasks queue; set TASKS_QUEUE_PATH env var.
6. Deploy container to Cloud Run; set SERVICE_URL env var to Cloud Run URL.
7. Configure Twilio WhatsApp sandbox and FCM server key for push.
