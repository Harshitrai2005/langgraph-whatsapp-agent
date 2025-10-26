from .base_agent import BaseAgent
from ..utils.preprocess import clean_text

class TextAgent(BaseAgent):
    """
    TextAgent processes text messages using a local LLM.
    """

    def __init__(self, name: str, model=None):
        super().__init__(name)
        self.model = model  # Placeholder for your local LLM

    def process(self, input_text: str) -> str:
        """
        Clean input text and generate a response using the LLM.
        """
        self.logger.info(f"Received input: {input_text}")

        # Step 1: Clean text
        cleaned_text = clean_text(input_text)
        self.logger.info(f"Cleaned text: {cleaned_text}")

        # Step 2: Generate response (here just echo for now)
        if self.model:
            # Use your local LLM here
            response = self.model.generate(cleaned_text)
        else:
            # Placeholder response for now
            response = f"Echo: {cleaned_text}"

        self.logger.info(f"Generated response: {response}")
        return response
