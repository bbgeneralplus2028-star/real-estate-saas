from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import psycopg2
import os

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")


# DATABASE CONNECTION (Neon)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)


# HEALTH CHECK
@app.get("/api/health")
def health():
    return {"status": "real estate SaaS running"}


# SAVE LEAD (CORE FEATURE)
@app.post("/api/lead")
async def save_lead(request: Request):
    data = await request.json()

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO leads (name, email, phone, message)
        VALUES (%s, %s, %s, %s)
        """,
        (
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("message"),
        ),
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "lead saved"}
