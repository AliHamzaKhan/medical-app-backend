from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from app import models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=schemas.User)
def read_credits(
    *, 
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user's credits.
    """
    return current_user
