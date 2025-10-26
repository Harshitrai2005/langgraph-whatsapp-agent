from abc import ABC, abstractmethod
from src.utils.logger import get_logger

class BaseAgent(ABC):
    """
    Base class for all agents (text, image, video).
    All agents must implement the process method.
    """

    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    @abstractmethod
    def process(self, input_data):
        """
        Process the input_data and return the output.
        Must be implemented by child agents.
        """
        raise NotImplementedError("Each agent must implement the process method")
