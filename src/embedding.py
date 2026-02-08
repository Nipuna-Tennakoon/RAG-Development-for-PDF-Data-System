from ollama import embeddings
from src.config import RAGSettings

class EmbeddingManager:
    def __init__(self, model_name : str = RAGSettings.EMBEDDING_MODEL_NAME):
        
        self.model_name = model_name
        
    def generate_embeddings(self, text):
        
        embedding = embeddings(model = self.model_name,
                               prompt=text,
                               keep_alive=False)
        
        embedding_out = embedding['embedding']
        
        return embedding_out