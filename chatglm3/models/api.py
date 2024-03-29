import langchain_community
from langchain_community.llms.chatglm import ChatGLM

print(dir(langchain_community.llms.chatglm))

CHATGLM_API_KEY = "your_api_key"  
# CHATGLM_MODEL_PATH = "/path/to/chatglm/model"

def load_chatglm(use_api=True):
    if use_api and CHATGLM_API_KEY:
        return ChatGLM(model_name="ChatGLM-3", streaming=True, callback_manager=None, verbose=True, api_key=CHATGLM_API_KEY)
    else:
        # return ChatGLMFastChat(model_name="ChatGLM-3", streaming=True, callback_manager=None, verbose=True, model_path=CHATGLM_MODEL_PATH)
        print("api无效，请检查")
