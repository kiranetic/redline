from typing import List, Optional
from pydantic import BaseModel, Field


class CardInput(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="Optional card title or heading"
    )
    description: Optional[str] = Field(
        default=None,
        description="Optional card description or body text"
    )


class SectionInput(BaseModel):
    section_title: str = Field(
        ...,
        description="Title or heading of the section"
    )
    section_description: Optional[str] = Field(
        default=None,
        description="Optional paragraph describing the section"
    )
    cards: List[CardInput] = Field(
        ...,
        description="List of cards that belong to the section"
    )
    desired_image_count: int = Field(
        ...,
        gt=0,
        description="Number of images required for this seciton"
    )


class CardIntent(BaseModel):
    index: int
    intent: str


class SectionAnalysisResult(BaseModel):
    section_theme: str
    visual_mood: str
    cohesion_strategy: str
    card_intents: List[CardIntent]

