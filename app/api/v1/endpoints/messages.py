from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Message])
def read_messages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve messages.
    """
    if crud.user.is_superuser(current_user):
        messages = crud.message.get_multi(db, skip=skip, limit=limit)
    else:
        messages = crud.message.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return messages


@router.post("/", response_model=schemas.Message)
def create_message(
    *,
    db: Session = Depends(deps.get_db),
    message_in: schemas.MessageCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new message.
    """
    message = crud.message.create_with_owner(db=db, obj_in=message_in, owner_id=current_user.id)
    return message


@router.get("/{id}", response_model=schemas.Message)
def read_message(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get message by ID.
    """
    message = crud.message.get(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    if not crud.user.is_superuser(current_user) and (message.sender_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return message
