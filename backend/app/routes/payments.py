from fastapi import APIRouter
from app.stripe import create_checkout

router = APIRouter()

@router.get("/subscribe")
def subscribe(email: str):
    return {"checkout_url": create_checkout(email)}
