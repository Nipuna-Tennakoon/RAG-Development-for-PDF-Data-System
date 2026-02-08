import os
from dotenv import load_dotenv

load_dotenv()

class RAGSettings():


    EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME',"qwen3-embedding:0.6b") 
    CHUNK_SIZE = os.getenv('CHUNK_SIZE', 250)
    CHUNK_OVERLAP = os.getenv('CHUNK_OVERLAP', 20)