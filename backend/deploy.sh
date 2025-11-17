#!/usr/bin/env bash
set -e
PROJECT=Guardian Angel
REGION=europe-west1
IMAGE=gcr.io/$PROJECT/guardian-pulse:latest
# build
docker build -t $IMAGE .
docker push $IMAGE
# deploy Cloud Run (adjust service account, secrets via console or gcloud)
gcloud run deploy guardian-pulse --image $IMAGE --region $REGION --platform managed --set-env-vars="CLOUDSQL_CONNECTION_NAME=PROJECT:REGION:INSTANCE,DB_USER=postgres,DB_NAME=guardian_db,USE_VERTEX=false" --allow-unauthenticated
