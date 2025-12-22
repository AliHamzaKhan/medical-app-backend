from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.message import Message, MessageCreate
from app.crud.crud_message import message

router = APIRouter()

@router.post("/", response_model=Message)
def create_new_message(message_in: MessageCreate, db: Session = Depends(deps.get_db)):
    return message.create(db=db, obj_in=message_in)

@router.get("/{message_id}", response_model=Message)
def read_message(message_id: int, db: Session = Depends(deps.get_db)):
    db_message = message.get(db, id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.get("/", response_model=list[Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    messages = message.get_multi(db, skip=skip, limit=limit)
    return messages
