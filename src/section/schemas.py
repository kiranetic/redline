from pydantic import BaseModel
from typing import Optional


class SectionInput(BaseModel):
    title: str
    description: Optional[str] = None
    card_count: int
    page_copy: Optional[str] = None


class SectionOutput(BaseModel):
    context: str
    mood: str
    tone: str
    card_count: int

