from src.utils.logger import get_logger
from src.section.schemas import SectionInput, SectionAnalysisResult
from src.section.analyzer import SectionAnalyzer


logger = get_logger(__name__)


class SectionService:
    def __init__(self) -> None:
        self.analyzer = SectionAnalyzer()
    

    async def analyze_section(self, section_input: SectionInput) -> SectionAnalysisResult:
        logger.info("Received section analysis request")
        return await self.analyzer.analyze(section_input)
    
