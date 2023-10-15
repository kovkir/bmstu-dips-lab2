SELECT 'CREATE DATABASE ticket_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydb')\gexec
