from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings

CHUNK_SIZE=500
CHUNK_OVERLAP=50
DATA_PATH='data/'
DB_FAISS_PATH='vectorstore/db_faiss'
MODEL_NAME='sentence-transformers/all-MiniLM-L6-v2'

class VectorStoreBuilder:

    def build():
        loader = DirectoryLoader(DATA_PATH,
                                 glob='*.pdf',
                                 loader_cls=PyPDFLoader)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,
                                                       chunk_overlap=CHUNK_OVERLAP)
        texts = text_splitter.split_documents(documents)
        embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME,
                                           model_kwargs={'device': 'cpu'})
        vectorstore = FAISS.from_documents(texts, embeddings)
        vectorstore.save_local(DB_FAISS_PATH)


class VectorStoreLoader:

    def load():
        embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME,
                                           model_kwargs={'device': 'cpu'})
        vectordb = FAISS.load_local(DB_FAISS_PATH, embeddings)
        return vectordb