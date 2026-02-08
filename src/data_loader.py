""" All the files are laoding and make the chunks for embeddings """

import os
from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader
from langchain_community.document_loaders import TextLoader, csv_loader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader

class RAGDataLoader:
    
    def __init__(self, source_dir : str, chnuk_size : int = 250, chunk_overlap : int = 20):
        self.source_dir = source_dir
        self.chunk_size = chnuk_size
        self.chunk_overlap = chunk_overlap
        
    def _pdf_loader(self):
        loader = DirectoryLoader(
            self.source_dir,
            glob = "**/*.pdf",
            loader_cls=PyMuPDFLoader,
            show_progress=True,
            )
        documents = loader.load()
        return documents
            
    def _text_loader(self):
        loader = DirectoryLoader(
            self.source_dir,
            glob="**/*.txt",
            loader_cls=TextLoader,
            show_progress=True
        )
        documents = loader.load()
        return documents
    
    def file_loader(self):
        pdf_docs = self._pdf_loader()
        text_docs = self._text_loader()
        
        if pdf_docs is None and text_docs is None:
            return "The source directory is empty"

        elif pdf_docs is None:
            loaded_docs = text_docs
            
        elif text_docs is None:
            loaded_docs = pdf_docs 
        
        else:    
            loaded_docs = pdf_docs+text_docs
        
        return loaded_docs  
    
    def data_splitter(self, extracted_documents):
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap,
            separators=["/n/n", ",", "/n"],
            length_function = len 
        )
        
        chunk_text = splitter.split_documents(extracted_documents)
        
        return chunk_text
        
        
        
    
    
        
        