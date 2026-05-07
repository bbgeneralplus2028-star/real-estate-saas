from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import psycopg2

from auth import register_user, login_user
from stripe_payments import create_checkout_session

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

DATABASE_URL = os.getenv("DATABASE_URL")


def get_db():
    return psycopg2.connect(DATABASE_URL)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/dashboard")
def dashboard():
    return FileResponse("static/dashboard.html")


# AUTH
@app.post("/api/register")
async def register(request: Request):
    data = await request.json()
    return register_user(data["email"], data["password"])


@app.post("/api/login")
async def login(request: Request):
    data = await request.json()
    return login_user(data["email"], data["password"])


# STRIPE
@app.get("/api/checkout")
def checkout():
    return {"url": create_checkout_session(1)}


# LEADS + AI SCORE
@app.post("/api/lead")
async def lead(request: Request):
    data = await request.json()

    score = 80 if "cash" in data.get("message", "").lower() else 50

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO leads (user_id, name, email, phone, message, score)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (1, data["name"], data["email"], data["phone"], data["message"], score))

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "saved", "score": score}
