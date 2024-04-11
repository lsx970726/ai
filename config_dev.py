# 开发环境的配置文件
import os
from decouple import config

# 选择要使用的向量存储库类型
VECTOR_STORE_TYPE = config('VECTOR_STORE_TYPE', default='chroma')

# 向量存储库配置
VECTOR_STORE_CONFIGS = {
    'chroma': {
        'collection_name': config('CHROMA_COLLECTION_NAME', default='langchain')
    },
    'faiss': {},
    'weaviate': {
        'url': config('WEAVIATE_URL', default='http://localhost:8080'),
        'index_name': config('WEAVIATE_INDEX_NAME', default='Langchain')
    },
    'qdrant': {
        'url': config('QDRANT_URL', default='localhost:6333'),
        'collection_name': config('QDRANT_COLLECTION_NAME', default='langchain')
    },
    'atis': {
        'storage_path': config('ATIS_STORAGE_PATH', default='/path/to/storage/')
    },
    'pinecone': {
        'api_key': config('PINECONE_API_KEY'),
        'environment': config('PINECONE_ENVIRONMENT'),
        'index_name': config('PINECONE_INDEX_NAME')
    },
    'redis': {
        'redis_url': config('REDIS_URL', default='redis://localhost:6379')
    },
    'pgvector': {
        'connection_string': config('PGVECTOR_CONNECTION_STRING')
    },
    'milvus': {
        'collection_name': config('MILVUS_COLLECTION_NAME', default='langchain'),
        'connection_args': {
            'host': config('MILVUS_HOST', default='localhost'),
            'port': config('MILVUS_PORT', default='19530')
        }
    }
}