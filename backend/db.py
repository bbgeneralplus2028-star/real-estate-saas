import psycopg2
import os

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
