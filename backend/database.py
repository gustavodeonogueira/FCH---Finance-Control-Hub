import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "finance"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )
    