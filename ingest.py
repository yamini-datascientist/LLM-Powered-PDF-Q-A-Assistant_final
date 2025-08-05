import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import faiss
import numpy as np

class PDFIngestor:
    def __init__(self, embedding_model=None, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        self.embedding_model = embedding_model if embedding_model else OpenAIEmbeddings()
        self.index = None
        self.text_chunks = []
    
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    
    def chunk_text(self, text):
        return self.text_splitter.split_text(text)
    
    def build_faiss_index(self, texts):
        # Get embeddings for all chunks
        embeddings = self.embedding_model.embed_documents(texts)
        dim = len(embeddings[0])
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(dim)
        embeddings_np = np.array(embeddings).astype('float32')
        self.index.add(embeddings_np)
        
        # Store text chunks aligned with index
        self.text_chunks = texts
    
    def ingest(self, pdf_paths):
        all_texts = []
        for path in pdf_paths:
            text = self.extract_text_from_pdf(path)
            chunks = self.chunk_text(text)
            all_texts.extend(chunks)
        self.build_faiss_index(all_texts)
        
    def search(self, query, top_k=5):
        # Embed query
        query_embedding = np.array(self.embedding_model.embed_query(query)).astype('float32').reshape(1, -1)
        
        # Search FAISS index
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = [self.text_chunks[i] for i in indices[0]]
        return results
