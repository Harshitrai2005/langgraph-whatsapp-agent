import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = {
    "MODEL_NAME": "mistral",
    "DATA_PATH": os.path.join(BASE_DIR, "data/knowledge_base"),
    "EMBED_PATH": os.path.join(BASE_DIR, "data/embeddings"),
    "LOG_LEVEL": "INFO",
}
