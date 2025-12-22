from pydantic import BaseModel
from typing import List

class AiGeneratedText(BaseModel):
    name : str
    diagnosis: str
    treatment: str
    doctors_recommended: List[str]
    suggestions: List[str]
