from langchain.chains import RetrievalQA
from cliftonai.llm import LlmFactory
from cliftonai.vectorstore import VectorStoreLoader
from cliftonai.prompt import PromptFactory

RETURN_SOURCE_DOCUMENTS=True
VECTOR_COUNT=2

class ChainFactory:

    def create():
        vectordb = VectorStoreLoader.load()
        llm = LlmFactory.create()
        qa_prompt = PromptFactory.create()
        chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=vectordb.as_retriever(search_kwargs={'k': VECTOR_COUNT}),
                                           return_source_documents=RETURN_SOURCE_DOCUMENTS,
                                           chain_type_kwargs={'prompt': qa_prompt}
                                           )
        return chain
