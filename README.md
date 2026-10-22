Oct 21, 2026

- Create agents with n8n

Favourite Projects by popular votes:
- Project 5: Engineering Team (with CrewAI)
- Project 6: Sidekick (with LangGraph)
- Project 7: Agent Loop
- Project: Agentic Stock Trader

Setup:
uv self update # update uv
uv sync # install dependencies
uv python list # show all installed python binaries
uv add xxx # add a dependency
uv run script.py # run a python script, activating venv if needed. also runs "uv sync" in the background

Day 2
======
3 definitions of an AI Agent:

Sam Altman: AI systems that can do work for you independently. (Open AI Sam Altman)
Early 2025 consensus: AI system where an LLM controls the workflow (Anthropic, hugging Face)
Current view (2026): An LLM with tools in a loop to achieve a goal.

Agentic Systems:

Anthropic distinguish two types: 
  - Workflows: are systems where LLMs and tools are orchestrated through predefined code paths.

  - Agents: are dynamic systems where LLMs direct their own processes and tool usage, maintaining control over how they accomplish tasks.

  However, they are both Agentic systems.

5 workflow design patterns:

1. Prompt Chaining: Decompose into fixed sub-tasks
2. Routing: Direct an input into a specialized sub-task, ensuring separation of concerns.
3. Parallelization: Breaking down tasks and running multiple subtasks concurrently
4. Orchestrator-Worker: Complex tasks are broken down dynamically and combined.
5. Evaluator-Optimizer (LLM as a judge): llM output is validated by another

By contrast, Agents:
1. Open-ended
2. Feedback loops
3. No fixed path

Risks of Agentic Frameworks:
1. Unpredictable path
2. Unpredictable output
3. Unpredictable costs

Mitigations for the risks:
1. Monitor (observability, Evals)
2. Guardrails: ensure your agents behave safely, consistently, and within your intended boundaries.

Agentic Traps:
1. Start from a problem that can be solved. Use agents only if there is a solution to the problem.
2. Anthropomorphizing (treating an agent like a human): A common red flag: "Agent architecture that assign human -like responsibilities to Agents. 
  Solution: 
  - Always start simple (one LLM)
  - Measure performance against business objective
  - Add agents because it improves performance

Takeaways:
- Build agent systems to solve problems in a measurable way
- Decide your agent architecture based on performance
- LLMs generate plausible outputs, not necessarily accurate outputs. Aligning the outputs with business results? That's your job.

Confusing Terminology:
- Agentic Engineer: someone who uses Agents to Engineer OR someone who engineers Agents

Models (ordered in increasing size left to right):
- OpenAI: GPT nano, GPT mini, GPT
- Anthropic: Clause Haiku, Claude Sonnet, Claude Opus 
- Google: Gemini Flash Lite, Gemini Flash, Gemini Pro
- DeepSeek AI: DeepSeek V4
Others:
- Groq: cloud LLM provider of pen-source LLMs (really fast, has nothing to do with Grok of Elon Musk)
- Grok: X AI's model
- Ollama: local open-source models
- OpenRouter
- Artificial Analysis: gives a comparison of the intelligence and costs of models (artificialanalysis.ai)

----

ollama serve
ollama ls
ollama pull xxx
ollama rm xxx





