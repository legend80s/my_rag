from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv


# 加载 .env 文件
load_dotenv()

# 设置 API Key
# os.environ["DASHSCOPE_API_KEY"] = "your-api-key"

# 初始化嵌入模型
dashscope_embeddings = DashScopeEmbeddings(
   model="text-embedding-v3",  # 或 "text-embedding-v2"，推荐 v3
    # model="text-embedding-v2",  # 或 "text-embedding-v2"，推荐 v3
)

# 直接使用
# result = embeddings.embed_query("你好，世界")
# print(result[:5])  # 输出向量前5维
