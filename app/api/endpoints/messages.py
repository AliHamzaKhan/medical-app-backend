from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.message import Message, MessageCreate
from app.crud.message import get_message, get_messages, create_message

router = APIRouter()

@router.post("/", response_model=Message)
def create_new_message(message: MessageCreate, db: Session = Depends(deps.get_db)):
    return create_message(db=db, message=message)

@router.get("/{message_id}", response_model=Message)
def read_message(message_id: int, db: Session = Depends(deps.get_db)):
    db_message = get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.get("/", response_model=list[Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    messages = get_messages(db, skip=skip, limit=limit)
    return messages
