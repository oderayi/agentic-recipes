import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

load_dotenv(override=True)

# Load API keys of various model providers from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# Print the status of each API key
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

if grok_api_key:
    print(f"Grok API Key exists and begins {grok_api_key[:4]}")
else:
    print("Grok API Key not set (and this is optional)")

if openrouter_api_key:
    print(f"OpenRouter API Key exists and begins {openrouter_api_key[:6]}") 
else:
    print("OpenRouter API Key not set (and this is optional)")

# Generate a challenging question for LLM evaluation
request = """
Please come up with a challenging, nuanced question with a succinct answer,
that I can ask a number of LLMs to evaluate their intelligence.
Not a mathematical puzzle, but more of a thought-provoking question that requires intelligent insight.
Include in your question that the answer must be short.
"""
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]

# Initialize the OpenAI client 
openai = OpenAI()

response = openai.chat.completions.create(model="gpt-5.5", messages=messages)
question = response.choices[0].message.content
Console().print(Markdown(f"{question}"))

# OpenAI Compatible URLs for other model providers
ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROK_BASE_URL = "https://api.x.ai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Initialize OpenAI clients for various model providers
anthropic = OpenAI(api_key=anthropic_api_key, base_url=ANTHROPIC_BASE_URL)
deepseek = OpenAI(api_key=deepseek_api_key, base_url=DEEPSEEK_BASE_URL)
gemini = OpenAI(api_key=google_api_key, base_url=GEMINI_BASE_URL)
groq = OpenAI(api_key=groq_api_key, base_url=GROQ_BASE_URL)
grok = OpenAI(api_key=grok_api_key, base_url=GROK_BASE_URL)
openrouter = OpenAI(api_key=openrouter_api_key, base_url=OPENROUTER_BASE_URL)
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

# Define a list of competitors and their corresponding answers
competitors = []
answers = []
messages = [{"role": "user", "content": question}]


# Function to record the model's answer and display it
def record(model_name, answer):
    competitors.append(model_name)
    answers.append(answer)
    Console().print(Markdown(f"{answer}"))

# Ask each model provider to answer the question and record their responses

# OpenAI GPT-5.4-nano 
model_name = "gpt-5.4-nano"
response = openai.chat.completions.create(model=model_name, messages=messages, reasoning_effort="none")
answer = response.choices[0].message.content
record(model_name, answer)

# Anthropic Claude-Sonnet-4-6
model_name = "claude-sonnet-4-6"
response = anthropic.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Gemini-3-flash-preview
model_name = "gemini-3-flash-preview"
response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# DeepSeek deepseek-v4-flash
model_name = "deepseek-v4-flash"
response = deepseek.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Groq gpt-oss-120b
model_name = "openai/gpt-oss-120b"
response = groq.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# OpenRouter moonshotai/kimi-k2.6
model_name = "moonshotai/kimi-k2.6"
response = openrouter.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Ollama llama2:latest
model_name = "llama2:latest"
response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Ollama gpt-oss:latest
model_name = "gpt-oss:latest"
response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Ollama gemma4:latest
model_name = "gemma4:latest"
response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
record(model_name, answer)

# Print the answers from all competitors
for competitor, answer in zip(competitors, answers):
    print(f"Competitor: {competitor}\n\n{answer}")

together = ""
for index, answer in enumerate(answers):
    together += f"# Response from competitor {index+1}\n\n"
    together += answer + "\n\n"


# Create a prompt for the LLM to judge the competitors' responses
judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{together}

Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""

judge_messages = [{"role": "user", "content": judge}]

# Judgement time!
# Grok is "The most truth-seeking large language model in the world."
model_name = "grok-4.3"
response = grok.chat.completions.create(model=model_name, messages=judge_messages)
results = response.choices[0].message.content

# Print the results of the judgement
results_dict = json.loads(results)
ranks = results_dict["results"]
for index, result in enumerate(ranks):
    competitor = competitors[int(result)-1]
    print(f"Rank {index+1}: {competitor}")

