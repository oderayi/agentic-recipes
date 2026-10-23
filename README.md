Oct 21, 2026

# Agentic AI Learning Notes and Recipes

Day 1
===

- Create agents with n8n

**Favourite Projects by popular votes:**
- Project 5: Engineering Team (with CrewAI)
- Project 6: Sidekick (with LangGraph)
- Project 7: Agent Loop
- Project: Agentic Stock Trader

**Setup:**

```bash
uv self update # update uv.  
uv sync # install dependencies. 
uv python list # show all installed python binaries.  
uv add xxx # add a dependency.  
uv run script.py # run a python script, activating venv if needed. also runs "uv sync" in the background
uv run python -m app.module.hello # to add repo root to sys.path and fix local import issues

```

Day 2
===
**3 definitions of an AI Agent:**

Sam Altman: AI systems that can do work for you independently. (Open AI Sam Altman)
Early 2025 consensus: AI system where an LLM controls the workflow (Anthropic, hugging Face)
Current view (2026): An LLM with tools in a loop to achieve a goal.

**Agentic Systems:**

__Anthropic distinguish two types:__ 
  - __Workflows__: are systems where LLMs and tools are orchestrated through predefined code paths.

  - __Agents__: are dynamic systems where LLMs direct their own processes and tool usage, maintaining control over how they accomplish tasks.

  However, they are both Agentic systems.

**5 workflow design patterns:**

1. Prompt Chaining: Decompose into fixed sub-tasks
2. Routing: Direct an input into a specialized sub-task, ensuring separation of concerns.
3. Parallelization: Breaking down tasks and running multiple subtasks concurrently
4. Orchestrator-Worker: Complex tasks are broken down dynamically and combined.
5. Evaluator-Optimizer (LLM as a judge): llM output is validated by another

**By contrast, Agents:**
1. Open-ended
2. Feedback loops
3. No fixed path

**Risks of Agentic Frameworks:**
1. Unpredictable path
2. Unpredictable output
3. Unpredictable costs

**Mitigations for the risks:**
1. Monitor (observability, Evals)
2. Guardrails: ensure your agents behave safely, consistently, and within your intended boundaries.

**Agentic Traps:**
1. Start from a problem that can be solved. Use agents only if there is a solution to the problem.
2. Anthropomorphizing (treating an agent like a human): A common red flag: "Agent architecture that assign human -like responsibilities to Agents. 
  Solution: 
  - Always start simple (one LLM)
  - Measure performance against business objective
  - Add agents because it improves performance

**Takeaways:**
- Build agent systems to solve problems in a measurable way
- Decide your agent architecture based on performance
- LLMs generate plausible outputs, not necessarily accurate outputs. Aligning the outputs with business results? That's your job.

**Confusing Terminology:**
- Agentic Engineer: someone who uses Agents to Engineer OR someone who engineers Agents

**Models (ordered in increasing size left to right):**
- OpenAI: GPT nano, GPT mini, GPT
- Anthropic: Clause Haiku, Claude Sonnet, Claude Opus 
- Google: Gemini Flash Lite, Gemini Flash, Gemini Pro
- DeepSeek AI: DeepSeek V4. 

**Others:** 
- Groq: cloud LLM provider of open-source LLMs (really fast, has nothing to do with Grok of Elon Musk)
- Grok: X AI's model
- Ollama: local open-source models
- OpenRouter
- Artificial Analysis: gives a comparison of the intelligence and costs of models (artificialanalysis.ai)

----
```bash
ollama serve
ollama ls
ollama pull xxx
ollama rm xxx
```

Day 3
===
Develop LLM-as-a-judge recipe (See [src/agentic-track/llm_as_a_judge](src/agentic-track/llm_as_a_judge)).

Day 4
===

**The Agent Landscape**

Differennt types of offering related to AI agents:

1. Builders (non-technical people can build AI Agents) e.g n8n, ElevenLabs, OpenAI Agent Builder, CrewAI Studio

2. Products (Non-technical people can use AI Agents) e.g Claude Code, Cowork, OpenClaw, Claude Design

3. Runtimes (Technical people can execute AI Agents) e.g AWS Lambda, AWS Bedrock AgentCore, Claude Managed Agents, Vertex AI Agent Engine

4. Frameworks (Technical people can develop AI Agents) e.g OpenAI Agents SDK, CrewAI, LangGraph/LangChani, Google ADK

**Agent Frameworks**

Helper code that makes it easier to create Agents based on LLM calls.
What frameworks offer:

- Orchestration - chanining together LLM calls
- Tool calling - equipping an LLM with abilities, including with MCP
- Constructing LLM inputs and interpreting outputs - including a technique called "Structured Output"

This allows you to easily code an 'Agent Loop' - an LLM in a loop with tools to achieve a goal.

**Framework categories**

- Lightweight: OpenAI Agents SDK, Google ADK, AWS Strands Agents. 
- Opinionated (less flexible): CrewAI, LangGraph/LangChain
- No framework at all

There are many more.


"Tools" give LLMs abilities.

The power to carry out actions like query a database or look up stock prices.

Tool Calling - in theory

An LLM equiped with a tool seems magical

It is Software that calls the tools not the LLM.

**Summary**
Agentic AI involves building a harness around LLMs crafting the inputs and interpreting the outputs, in a loop, so that they can 'use tools' and 'be autonomous'.

Agent Frameworks are helper code that make it faster to implement these techniques, but they're not required.

Day 5
===

Context Engineering vs Prompt Engineering
