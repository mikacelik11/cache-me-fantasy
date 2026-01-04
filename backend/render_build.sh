#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Run database migrations (create tables)
python -c "from app.database import engine; from app.models import Base; Base.metadata.create_all(bind=engine)"

# Seed initial players
python -m app.add_all_nba_players
