# main.py
import os, time, json, hmac, hashlib, base64
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
import httpx
from twilio.rest import Client as TwilioClient
from google.cloud import secretmanager
from google.cloud.sql.connector import Connector
import sqlalchemy
from cryptography.fernet import Fernet
from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2


# Vertex AI optional
try:
from google.cloud import aiplatform
except Exception:
aiplatform = None


# ========== CONFIG ==========
PROJECT_ID = os.getenv("GCP_PROJECT") or os.getenv("GOOGLE_CLOUD_PROJECT")
REGION = os.getenv("REGION", "asia-south1")
CLOUDSQL_CONNECTION_NAME = os.getenv("CLOUDSQL_CONNECTION_NAME")
DB_USER = os.getenv("DB_USER", "postgres")
DB_NAME = os.getenv("DB_NAME", "guardian_db")


SECRET_TWILIO_SID = os.getenv("SECRET_TWILIO_SID", "TWILIO_SID")
SECRET_TWILIO_TOKEN = os.getenv("SECRET_TWILIO_TOKEN", "TWILIO_TOKEN")
SECRET_TWILIO_FROM = os.getenv("SECRET_TWILIO_FROM", "TWILIO_FROM")
SECRET_EMERGENCY_CONTACTS = os.getenv("SECRET_EMERGENCY_CONTACTS", "EMERGENCY_CONTACTS_JSON")
SECRET_HMAC_KEY = os.getenv("SECRET_HMAC_KEY", "HMAC_KEY")
SECRET_FERNET_KEY = os.getenv("SECRET_FERNET_KEY", "FERNET_KEY")
USE_VERTEX = os.getenv("USE_VERTEX", "false").lower() == "true"
VERTEX_MODEL = os.getenv("VERTEX_MODEL", "text-bison@001")


TRIGGER_WORDS = [w.strip().lower() for w in os.getenv("TRIGGER_WORDS", "help,help me,sos,emergency,danger").split(",")]
ESCALATION_MINUTES = int(os.getenv("ESCALATION_MINUTES", "3"))


# ========== Helpers ==========
sm_client = secretmanager.SecretManagerServiceClient()


def access_secret(name: str) -> str:
path = f"projects/{PROJECT_ID}/secrets/{name}/versions/latest"
resp = sm_client.access_secret_version(request={"name": path})
return resp.payload.data.decode("utf-8")


# Load secrets
TWILIO_SID = os.getenv("TWILIO_SID") or access_secret(SECRET_TWILIO_SID)
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN") or access_secret(SECRET_TWILIO_TOKEN)
TWILIO_FROM = os.getenv("TWILIO_FROM") or access_secret(SECRET_TWILIO_FROM)
EMERGENCY_CONTACTS_JSON = os.getenv("EMERGENCY_CONTACTS_JSON") or access_secret(SECRET_EMERGENCY_CONTACTS)
HMAC_KEY = os.getenv("HMAC_KEY") or access_secret(SECRET_HMAC_KEY)
FERNET_KEY = os.getenv("FERNET_KEY") or access_secret(SECRET_FERNET_KEY)


# Twilio client
twilio = TwilioClient(TWILIO_SID, TWILIO_TOKEN)
connector = Connector()


def getconn():
return connector.connect(CLOUDSQL_CONNECTION_NAME, "pg8000", user=DB_USER, password=os.getenv("DB_PASS"), db=DB_NAME)


results["dispatched"] = True
