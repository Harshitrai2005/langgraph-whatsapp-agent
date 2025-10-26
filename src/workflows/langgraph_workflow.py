from src.agents.text_agent import TextAgent
from src.agents.image_agent import ImageAgent
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
        # Initialize agents
        self.text_agent = TextAgent("TextAgent")
        self.text_agent.kb = self.kb  # Attach KB to text agent
        self.image_agent = ImageAgent("ImageAgent")
        # Future: self.video_agent = VideoAgent("VideoAgent")

    def process_text(self, message: str) -> str:
        """
        Process text messages through TextAgent with KB retrieval.
        """
        self.logger.info(f"Processing text message: {message}")
        response = self.text_agent.process(message)
        return response

    def process_image(self, image_path: str) -> str:
        """
        Process images through ImageAgent.
        """
        self.logger.info(f"Processing image: {image_path}")
        response = self.image_agent.process(image_path)
        return response
