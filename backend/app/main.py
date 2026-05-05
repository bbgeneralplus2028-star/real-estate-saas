from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, properties, ai, payments

app = FastAPI(title="Real Estate SaaS")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(users.router, prefix="/api/users")
app.include_router(properties.router, prefix="/api/properties")
app.include_router(ai.router, prefix="/api/ai")
app.include_router(payments.router, prefix="/api/payments")


@app.get("/")
def root():
    return {"status": "real estate SaaS running"}
