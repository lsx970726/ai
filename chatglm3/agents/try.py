from langchain.agents import initialize_agent, Tool
from langchain.utilities import SerpAPIWrapper
from chatglm3.models.api import load_chatglm
# 加载 ChatGLM 模型
llm = load_chatglm(use_api=True)

# 定义搜索工具
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="Useful for searching up-to-date information on the internet."
    )
]

# 初始化 Agent
news_agent = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True)

# 使用 Agent 回答问题
query = "最近有哪些重大新闻事件?"
result = news_agent.run(query)
print(result)