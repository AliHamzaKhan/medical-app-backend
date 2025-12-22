from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Shared properties
class MedicineSearchHistoryBase(BaseModel):
    search_query: Optional[str] = None
    search_timestamp: Optional[datetime] = None


# Properties to receive on item creation
class MedicineSearchHistoryCreate(MedicineSearchHistoryBase):
    user_id: int
    search_query: str


# Properties to receive on item update
class MedicineSearchHistoryUpdate(MedicineSearchHistoryBase):
    pass


# Properties shared by models in DB
class MedicineSearchHistoryInDBBase(MedicineSearchHistoryBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class MedicineSearchHistory(MedicineSearchHistoryInDBBase):
    pass


# Properties properties stored in DB
class MedicineSearchHistoryInDB(MedicineSearchHistoryInDBBase):
    pass
