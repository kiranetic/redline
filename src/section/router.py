from fastapi import APIRouter
from src.section.schemas import SectionInput, SectionOutput
from src.section.service import SectionService


router = APIRouter()
service = SectionService()


@router.post("/analyze", response_model=SectionOutput)
async def analyze_section(section: SectionInput):
    return await service.analyze_section(section)

