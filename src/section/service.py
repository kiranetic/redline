from src.section.agent import SectionAnalyzer
from src.section.schemas import SectionInput, SectionOutput


class SectionService:
    def __init__(self) -> None:
        self.analyzer = SectionAnalyzer()
    

    async def analyze_section(self, section: SectionInput) -> SectionOutput:
        return await self.analyzer.analyze(section)
    
