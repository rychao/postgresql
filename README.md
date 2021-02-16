# Riot Games API + Postgres

This projects involves Python to interact with the Riot Games API and involves pushing it to a SQL database in GCP. We then use Flask to fetch data as a json and push it to an API layer.

### Requires
- Psycopg2
- Riotwatcher API
- Riot Games API key
- Terraform
- Flask
- Database (GCP)

### Scripts
- main.tf - provisions SQL database in GCP
- api.py - Using Flask, fetches data from SQL to publish an api layer
