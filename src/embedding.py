from ollama import embeddings


class EmbeddingManager:
    def __init__(self, model_name : str = "qwen3-embedding:0.6b", ):
        
        self.model_name = model_name
        
    def generate_embeddings(self, text):
        
        embedding = embeddings(model = self.model_name,
                               prompt=text,
                               keep_alive=False)
        
        embedding_out = embedding['embedding']
        
        return embedding_out