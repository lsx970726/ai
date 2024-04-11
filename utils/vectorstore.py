# 向量存储库
from langchain_community.vectorstores import Chroma, FAISS, Weaviate, Qdrant, Pinecone, Redis, PGVector, Milvus
import pinecone
import chromadb

def get_vector_store(store_type, **kwargs):
    if store_type == "chroma":
        # 创建 Chroma 向量存储库
        chroma_client = chromadb.Client()
        return Chroma(chroma_client=chroma_client, collection_name=kwargs.get('collection_name', 'langchain'))
    
    elif store_type == "faiss":
        # 创建 FAISS 向量存储库
        return FAISS.from_texts(texts=kwargs['texts'], embedding=kwargs['embedding'])
    
    elif store_type == "weaviate":
        # 创建 Weaviate 向量存储库
        weaviate = Weaviate(url=kwargs.get('url', "http://localhost:8080"), index_name=kwargs.get('index_name', "Langchain"))
        weaviate.add_texts(kwargs['texts'], kwargs['embedding'])
        return weaviate

    elif store_type == "qdrant":
        # 创建 Qdrant 向量存储库
        return Qdrant.from_texts(texts=kwargs['texts'], embeddings=kwargs['embedding'], url=kwargs.get('url', "localhost:6333"), collection_name=kwargs.get('collection_name', "langchain"))

    elif store_type == "atis":
        # 创建 ATIS 向量存储库
        return ATIS.from_texts(texts=kwargs['texts'], embedding=kwargs['embedding'], storage_context_params={"path": kwargs.get('storage_path', "/path/to/storage/")})

    elif store_type == "pinecone":
        # 创建 Pinecone 向量存储库
        pinecone.init(api_key=kwargs['api_key'], environment=kwargs['environment'])
        index = pinecone.Index(kwargs['index_name'])
        return Pinecone(index, kwargs['texts'], kwargs['embedding'].embed_query)

    elif store_type == "redis":
        # 创建 Redis 向量存储库
        return Redis.from_texts(texts=kwargs['texts'], embeddings=kwargs['embedding'], redis_url=kwargs.get('redis_url', "redis://localhost:6379"))

    elif store_type == "pgvector":
        # 创建 PGVector 向量存储库
        return PGVector.from_texts(texts=kwargs['texts'], embeddings=kwargs['embedding'], connection_string=kwargs['connection_string'])

    elif store_type == "milvus":
        # 创建 Milvus 向量存储库
        return Milvus.from_texts(texts=kwargs['texts'], embeddings=kwargs['embedding'], collection_name=kwargs.get('collection_name', "langchain"), connection_args=kwargs.get('connection_args', {"host": "localhost", "port": "19530"}))
    
    else:
        raise ValueError(f"Invalid vector store type: {store_type}")