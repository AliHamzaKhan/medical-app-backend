
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_doctors():
    return [{"doctor_id": 1, "name": "Dr. Smith"}]
