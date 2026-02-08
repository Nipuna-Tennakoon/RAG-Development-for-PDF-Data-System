from src.data_loader import RAGDataLoader
from src.embedding import EmbeddingManager

source_dir = "data/pdf_files"
# dataloader = RAGDataLoader(source_dir=source_dir)

# loaded_docs = dataloader.file_loader()

# print(len(loaded_docs))

# split_text = dataloader.data_splitter(extracted_documents=loaded_docs)

# print(len(split_text))

text = "I love you kesaroo"

embedding_manager = EmbeddingManager()

print(embedding_manager.generate_embeddings(text))