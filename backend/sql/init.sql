CREATE TABLE IF NOT EXISTS alerts (
  id SERIAL PRIMARY KEY,
  user_id TEXT,
  name TEXT,
  phone TEXT,
  latitude double precision,
  longitude double precision,
  prompt TEXT,
  responder TEXT,
  responder_confidence double precision,
  responder_choice_json JSONB,
  encrypted_payload TEXT,
  acknowledged boolean DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
