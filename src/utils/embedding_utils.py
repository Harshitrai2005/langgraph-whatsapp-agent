import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

from src.utils.config import CONFIG

class KnowledgeBase:
    """
    Simple KB using TF-IDF embeddings.
    """

    def __init__(self, kb_folder=CONFIG["DATA_PATH"]):
        self.kb_folder = kb_folder
        self.texts = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.load_texts()
        self.build_embeddings()

    def load_texts(self):
        """
        Load all text files from kb_folder
        """
        for file in os.listdir(self.kb_folder):
            if file.endswith(".txt"):
                with open(os.path.join(self.kb_folder, file), "r", encoding="utf-8") as f:
                    self.texts.append(f.read())

    def build_embeddings(self):
        """
        Build TF-IDF matrix for retrieval
        """
        self.tfidf_matrix = self.vectorizer.fit_transform(self.texts)

    def query(self, message: str, top_k=1):
        """
        Return top_k most similar texts from KB
        """
        query_vec = self.vectorizer.transform([message])
        import numpy as np
        from sklearn.metrics.pairwise import cosine_similarity

        similarities = cosine_similarity(query_vec, self.tfidf_matrix)
        top_indices = np.argsort(similarities[0])[::-1][:top_k]
        results = [self.texts[i] for i in top_indices]
        return results
