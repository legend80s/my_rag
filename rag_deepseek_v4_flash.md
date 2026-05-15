```py
❯ uv run main.py
USER_AGENT environment variable not set, consider setting it to identify your requests.
Total characters: 43047


      LLM Powered Autonomous Agents

Date: June 23, 2023  |  Estimated Reading Time: 31 min  |  Author: Lilian Weng


Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
Agent System Overview#
In
Split blog post into 63 sub-documents.
['0f5dc87b-6e31-4e0e-8962-5c1ca83ef0d6', '4f2adba2-3999-4da5-b2aa-6032fedc01db', '1aefa328-6813-45e8-bb65-ee11ea12af9f']
================================ Human Message =================================

What is task decomposition?
================================== Ai Message ==================================

Let me retrieve some context about task decomposition.
Tool Calls:
  retrieve_context (call_00_7q5HoDInJ6qJHgi66vLf7670)
 Call ID: call_00_7q5HoDInJ6qJHgi66vLf7670
  Args:
    query: task decomposition
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: pytest
dataclasses

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Pseudo code of how LLM makes an API call in API-Bank. (Image source: Li et al. 2023)

In the API-Bank workflow, LLMs need to make a couple of decisions and at each step we can evaluate how accurate that decision is. Decisions include:

Whether an API call is needed.
Identify the right API to call: if not good enough, LLMs need to iteratively modify the API inputs (e.g. deciding search keywords for Search Engine API).
Response based on the API results: the model can choose to refine and call again if results are not satisfied.

This benchmark evaluates the agent’s tool use capabilities at three levels:
================================== Ai Message ==================================

The context doesn't have a clear definition of task decomposition. Let me try to find more relevant information.
Tool Calls:
  retrieve_context (call_00_PPN6IpkWZS49byCsFuWk0750)
 Call ID: call_00_PPN6IpkWZS49byCsFuWk0750
  Args:
    query: task decomposition definition
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: "content": "Please now remember the steps:\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\n\nThen you will output the content of each file including ALL code.\nEach file must strictly follow a markdown code block format, where the following tokens must be replaced such that\nFILENAME is the lowercase file name including the file extension,\nLANG is the markup code block language for the code's language, and CODE is the code:\n\nFILENAME\n```LANG\nCODE\n```\n\nPlease note that the code should be fully functional. No placeholders.\n\nYou will start with the \"entrypoint\" file, then go to the ones that are imported by that file, and so on.\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc. The code should be fully

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: LLM Powered Autonomous Agents

Date: June 23, 2023  |  Estimated Reading Time: 31 min  |  Author: Lilian Weng


Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
Agent System Overview#
In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:

Planning

Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.
Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results.


Memory
================================== Ai Message ==================================

Based on the retrieved context, here's an explanation of **task decomposition**:

Task decomposition is a key component of **planning** in LLM-powered autonomous agent systems. It refers to the process where the agent breaks down large, complex tasks into smaller, more manageable subgoals or subtasks. This enables the agent to efficiently handle complex tasks by tackling them step by step rather than attempting to solve everything at once.

In the context of autonomous agents (like AutoGPT, GPT-Engineer, and BabyAGI), task decomposition works alongside other planning components such as **reflection and refinement** (where the agent self-criticizes, learns from mistakes, and improves future steps) and **memory** to create a robust problem-solving system.

my_rag on 🌱 main [!] is 📦 v0.1.0 via 🐍 v3.13.3 liuchzong@qq.com took 19s
```
