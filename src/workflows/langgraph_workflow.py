from src.agents.text_agent import TextAgent
from src.utils.logger import get_logger
from src.utils.embedding_utils import KnowledgeBase

class LangGraphWorkflow:
    """
    Orchestrates multiple agents (text, image, video) for WhatsApp AI agent.
    """

    def __init__(self):
        self.logger = get_logger("LangGraphWorkflow")
        # Initialize knowledge base
        self.kb = KnowledgeBase()
        # Initialize agents with KB
        self.text_agent = TextAgent("TextAgent")
        self.text_agent.kb = self.kb  # Attach KB to agent
        # Future: self.image_agent = ImageAgent("ImageAgent")
        # Future: self.video_agent = VideoAgent("VideoAgent")

    def process_text(self, message: str) -> str:
        """
        Process text messages through TextAgent with KB retrieval.
        """
        self.logger.info(f"Processing message: {message}")
        response = self.text_agent.process(message)
        return response
