import sys

# # Stage 1: Foundation
# from src.config import llm
# print(llm.invoke("Hello, how are you?").content)
# sys.exit()


# # Stage 2
# from src.tools import search_product_catalog
# print(search_product_catalog.invoke({"query": "wireless head phones"}))
# sys.exit()


# Stage 3
from langchain_core.messages import HumanMessage, SystemMessage
from src.nodes import product_subgraph, PRODUCT_PROMPT
result = product_subgraph.invoke({'message': [
    SystemMessage(content=PRODUCT_PROMPT),
    HumanMessage(content='Show me headphones under 15000')]})
print(result['messages'][-1].content)
sys.exit()