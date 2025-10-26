from src.agents.base_agent import BaseAgent
from src.utils.logger import get_logger
from PIL import Image

class ImageAgent(BaseAgent):
    """
    ImageAgent processes images for text extraction or analysis.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def process(self, image_path: str) -> str:
        """
        Process an image and return extracted info.
        """
        self.logger.info(f"Processing image: {image_path}")
        try:
            img = Image.open(image_path)
            # Placeholder: return image size
            result = f"Image size: {img.size}"
        except Exception as e:
            self.logger.error(f"Error processing image: {e}")
            result = "Failed to process image"
        self.logger.info(f"Processed result: {result}")
        return result
