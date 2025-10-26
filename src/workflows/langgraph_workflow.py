from src.agents.text_agent import TextAgent
from src.utils.logger import get_logger

class LangGraphWorkflow:
    """
    Orchestrates multiple agents (text, image, video) for WhatsApp AI agent.
    """

    def __init__(self):
        self.logger = get_logger("LangGraphWorkflow")
        # Initialize agents
        self.text_agent = TextAgent("TextAgent")
        # Future: self.image_agent = ImageAgent("ImageAgent")
        # Future: self.video_agent = VideoAgent("VideoAgent")

    def process_text(self, message: str) -> str:
        """
        Process text messages through TextAgent.
        """
        self.logger.info(f"Processing message: {message}")
        response = self.text_agent.process(message)
        return response
