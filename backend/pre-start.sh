#! /usr/bin/env bash

# Let the DB start
 
python ./app/check_db_connection.py

# Run migrations

 
alembic upgrade head
 

# Create initial data in DB
python ./app/seed_db_with_initial_data.py
