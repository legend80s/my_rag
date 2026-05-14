# https://mydeepseekapi.com/blog/unlocking-power-deepseek-embedding-api-advanced-applications

import requests
import os
from dotenv import load_dotenv
import json

# 加载 .env 文件
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY_DEEP_SEEK_EMBEDDING")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# print(f"{headers=}")

data = {
    "input": "Explain how LLMs generate human-like text.",
    "model": "deepseek-embedding-v1",
}

response = requests.post(
    "https://api.deepseek.com/v1/embeddings", headers=headers, json=json.dumps(data)
)
response.raise_for_status()

resp = response.text

print(f"{resp=}")

# print(json["embedding"] if "embedding" in json else json["error"]["message"])
# print(response.json()["embedding"])
