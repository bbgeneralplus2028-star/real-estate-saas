from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
def search(q: str):
    return {
        "query": q,
        "results": [
            {"title": "Luxury Home", "price": 850000, "location": "NYC"},
            {"title": "Family House", "price": 420000, "location": "NJ"}
        ]
    }
