import re

def clean_text(text: str) -> str:
    """
    Clean and normalize input text for the agent.
    - Lowercase
    - Remove URLs
    - Remove special characters except spaces
    """
    text = text.lower()
    text = re.sub(r"http\S+", "", text)          # Remove URLs
    text = re.sub(r"[^a-z0-9\s]", "", text)     # Remove special characters
    return text.strip()
