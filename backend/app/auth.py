from fastapi import HTTPException
import psycopg2
import os
import hashlib

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email, password):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hash_password(password))
        )
        conn.commit()
    except:
        raise HTTPException(status_code=400, detail="User exists")

    cur.close()
    conn.close()
    return {"status": "user created"}


def login_user(email, password):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM users WHERE email=%s AND password=%s",
        (email, hash_password(password))
    )

    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid login")

    return {"user_id": user[0]}
