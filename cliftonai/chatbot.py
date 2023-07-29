import timeit
from cliftonai.chain import ChainFactory
from typing import NamedTuple

class ChatbotResponse(NamedTuple):
    question: str
    answer: str
    #source_documents: list
    response_time: float

class Chatbot:
    def __init__(self):
       self.chain = ChainFactory.create()

    def ask(self,question):
        start = timeit.default_timer()
        chain_response = self.chain({'query': question})
        end = timeit.default_timer()
        response = ChatbotResponse(
            question=question,
            answer=chain_response["result"],
            response_time=end - start
        ) 
        return response
