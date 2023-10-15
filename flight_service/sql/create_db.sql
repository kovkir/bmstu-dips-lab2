SELECT 'CREATE DATABASE flight_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydb')\gexec
