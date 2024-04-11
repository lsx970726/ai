from langchain.embeddings import OpenAIEmbeddings
from utils.vectorstore import get_vector_store
import os

# 加载配置
if os.environ.get('ENV') == 'production':
    from config_prod import *
else:
    from config_dev import *

# 加载文本数据
with open('xiyouji.txt', 'r', encoding='utf-8') as f:
    texts = f.read().split('\n')

# 初始化嵌入模型
embedding = OpenAIEmbeddings()

# 从配置文件中获取向量存储库类型和配置

vector_store_configs = VECTOR_STORE_CONFIGS.get(VECTOR_STORE_TYPE, {})
vector_store_configs['texts'] = texts
vector_store_configs['embedding'] = embedding

# 创建向量存储库实例
vector_store = get_vector_store(VECTOR_STORE_TYPE, **vector_store_configs)