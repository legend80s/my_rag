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
['cb0b54e4-c6b5-49dc-adf6-b79c8d66824d', 'c529dd52-7c06-463a-b0d6-ca80f92a5006', '4f70416f-3f19-4f35-aa47-2935b19f8ed2']
================================ Human Message =================================

What is task decomposition?
================================== Ai Message ==================================

Let me look up context about task decomposition.
Tool Calls:
  retrieve_context (call_00_BYChH2HWHVNfvhtb2fDC3316)
 Call ID: call_00_BYChH2HWHVNfvhtb2fDC3316
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
Tool Calls:
  retrieve_context (call_00_epOlcxUqARVNa4x8GlLc6826)
 Call ID: call_00_epOlcxUqARVNa4x8GlLc6826
  Args:
    query: task decomposition definition agent
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: MRKL (Karpas et al. 2022), short for “Modular Reasoning, Knowledge and Language”, is a neuro-symbolic architecture for autonomous agents. A MRKL system is proposed to contain a collection of “expert” modules and the general-purpose LLM works as a router to route inquiries to the best suitable expert module. These modules can be neural (e.g. deep learning models) or symbolic (e.g. math calculator, currency converter, weather API).
They did an experiment on fine-tuning LLM to call a calculator, using arithmetic as a test case. Their experiments showed that it was harder to solve verbal math problems than explicitly stated math problems because LLMs (7B Jurassic1-large model) failed to extract the right arguments for the basic arithmetic reliably. The results highlight when the external symbolic tools can work reliably, knowing when to and how to use the tools are crucial, determined by the LLM capability.

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: They also discussed the risks, especially with illicit drugs and bioweapons. They developed a test set containing a list of known chemical weapon agents and asked the agent to synthesize them. 4 out of 11 requests (36%) were accepted to obtain a synthesis solution and the agent attempted to consult documentation to execute the procedure. 7 out of 11 were rejected and among these 7 rejected cases, 5 happened after a Web search while 2 were rejected based on prompt only.
Generative Agents Simulation#
Generative Agents (Park, et al. 2023) is super fun experiment where 25 virtual characters, each controlled by a LLM-powered agent, are living and interacting in a sandbox environment, inspired by The Sims. Generative agents create believable simulacra of human behavior for interactive applications.
The design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.
================================== Ai Message ==================================
Tool Calls:
  retrieve_context (call_00_pYRlpJ36bsGgM7wijWUD5139)
 Call ID: call_00_pYRlpJ36bsGgM7wijWUD5139
  Args:
    query: "task decomposition" LLM agent planning
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: The generative agent architecture. (Image source: Park et al. 2023)

This fun simulation results in emergent social behavior, such as information diffusion, relationship memory (e.g. two agents continuing the conversation topic) and coordination of social events (e.g. host a party and invite many others).
Proof-of-Concept Examples#
AutoGPT has drawn a lot of attention into the possibility of setting up autonomous agents with LLM as the main controller. It has quite a lot of reliability issues given the natural language interface, but nevertheless a cool proof-of-concept demo. A lot of code in AutoGPT is about format parsing.
Here is the system message used by AutoGPT, where {{...}} are user inputs:
You are {{ai-name}}, {{user-provided AI bot description}}.
Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications.

GOALS:

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Resources:
1. Internet access for searches and information gathering.
2. Long Term memory management.
3. GPT-3.5 powered Agents for delegation of simple tasks.
4. File output.

Performance Evaluation:
1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
2. Constructively self-criticize your big-picture behavior constantly.
3. Reflect on past decisions and strategies to refine your approach.
4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.
================================== Ai Message ==================================
Tool Calls:
  retrieve_context (call_00_0JYp1wo3ucyRJVCj8u674844)
 Call ID: call_00_0JYp1wo3ucyRJVCj8u674844
  Args:
    query: task decomposition chain of thought plan subgoals
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.
Another quite distinct approach, LLM+P (Liu et al. 2023), involves relying on an external classical planner to do long-horizon planning. This approach utilizes the Planning Domain Definition Language (PDDL) as an intermediate interface to describe the planning problem. In this process, LLM (1) translates the problem into “Problem PDDL”, then (2) requests a classical planner to generate a PDDL plan based on an existing “Domain PDDL”, and finally (3) translates the PDDL plan back into natural language. Essentially, the planning step is outsourced to an external tool, assuming the availability of domain-specific PDDL and a suitable planner which is common in certain robotic setups but not in many other domains.
Self-Reflection#

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: After fine-tuning with CoH, the model can follow instructions to produce outputs with incremental improvement in a sequence. (Image source: Liu et al. 2023)

The idea of CoH is to present a history of sequentially improved outputs  in context and train the model to take on the trend to produce better outputs. Algorithm Distillation (AD; Laskin et al. 2023) applies the same idea to cross-episode trajectories in reinforcement learning tasks, where an algorithm is encapsulated in a long history-conditioned policy. Considering that an agent interacts with the environment many times and in each episode the agent gets a little better, AD concatenates this learning history and feeds that into the model. Hence we should expect the next predicted action to lead to better performance than previous trials. The goal is to learn the process of RL instead of training a task-specific policy itself.


Illustration of how Algorithm Distillation (AD) works. (Image source: Laskin et al. 2023).
================================== Ai Message ==================================

Based on the retrieved context, here's an explanation of **task decomposition**:

**Task decomposition** is the process of breaking down a large, complex task into smaller, more manageable subgoals or steps. In the context of LLM-based autonomous agents, it's a key planning mechanism.

According to the context, task decomposition can be done in three main ways:

1. **By LLM with simple prompting** – e.g., asking the model "Steps for XYZ.\n1." or "What are the subgoals for achieving XYZ?"
2. **Using task-specific instructions** – e.g., providing a domain-specific prompt like "Write a story outline" for novel writing.
3. **With human inputs** – where a human provides the decomposition manually.

There's also an approach called **LLM+P** (Liu et al. 2023) which outsources the planning step to an external classical planner using the Planning Domain Definition Language (PDDL) as an intermediate interface.

In essence, task decomposition helps agents handle complex, long-horizon tasks by turning them into a sequence of simpler steps that can be tackled one at a time.

my_rag on 🌱 main [!?] is 📦 v0.1.0 via 🐍 v3.13.3 (my-rag) liuchzong@qq.com took 9s 
```
