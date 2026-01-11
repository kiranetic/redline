from fastapi import APIRouter
from src.section.schemas import SectionInput, SectionAnalysisResult
from src.section.service import SectionService


router = APIRouter()

service = SectionService()


@router.post("/analyze", response_model=SectionAnalysisResult)
async def analyze_section(section_input: SectionInput) -> SectionAnalysisResult:
    return await service.analyze_section(section_input)

