from langchain.llms import CTransformers

MODEL_BIN_PATH='models/llama-2-7b-chat.ggmlv3.q8_0.bin'
MODEL_TYPE='llama'
MAX_NEW_TOKENS=256
TEMPERATURE=0.01   

class LlmFactory:

    def create():
        # Local CTransformers model
        llm = CTransformers(model=MODEL_BIN_PATH,
                            model_type=MODEL_TYPE,
                            config={'max_new_tokens': MAX_NEW_TOKENS,
                                    'temperature': TEMPERATURE}
                            )
        return llm
