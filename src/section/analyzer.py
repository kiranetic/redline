from src.utils.logger import get_logger
from src.section.schemas import (
    SectionInput,
    SectionAnalysisResult,
    CardIntent
)


logger = get_logger(__name__)


class SectionAnalyzer:
    """
    Responsible for understanding the intent and visual direction 
    of a website section.
    """

    async def analyze(self, data: SectionInput) -> SectionAnalysisResult:
        logger.info("Starting section analysis")
        logger.info(f"Analyzing section: {data.section_title} with {len(data.cards)}")

        section_theme = data.section_title
        visual_mood = "neutral"
        cohesion_strategy = "maintain consistent tone across all cards"

        card_intents = []
        for idx, card in enumerate(data.cards):
            intent_text = card.title or card.description or "general concept"
            logger.info(f"Derived intent for card {idx}: {intent_text}")
            card_intents.append(CardIntent(index=idx, intent=intent_text))
        
        logger.info("Completed section analysis")

        return SectionAnalysisResult(
            section_theme=section_theme,
            visual_mood=visual_mood,
            cohesion_strategy=cohesion_strategy,
            card_intents=card_intents
        )

