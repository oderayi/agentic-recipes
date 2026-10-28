# Simple Agent and Agent Loop with OpenAI Agents SDK
# Demonstrates session (memory) approaches (conversation lists and SQLiteSession) and tools with OpenAI Agents SDK


import asyncio
import os

import requests
from agents import Agent, Runner, SQLiteSession, function_tool, trace
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv(override=True)


# Make an agent with name, instructions, model
agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-5.4-mini")

# Run the joke with Runner.run(agent, prompt)
async def tell_joke():
  return await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
result = asyncio.run(tell_joke())

# Here is the final output
print(result.final_output)

# Here is the detail of the LLM calls
result.to_input_list()

# Adding observability with trace
async def tell_joke_with_trace():
  with trace("Telling a joke"):
      return await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
result = asyncio.run(tell_joke_with_trace())
print(result.final_output)

# See the traces here https://platform.openai.com/traces

# Streaming
async def tell_jokes_streamed():
    result = Runner.run_streamed(agent, input="Please tell me 5 jokes about AI Agents.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(tell_jokes_streamed())

## Adding Tools to the Agent

# Test pushover configuration
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

if pushover_user:
    if pushover_user.startswith("u"):
        print("Pushover user found and looks good")
    else:
        print("Pushover user found but doesn't start with u")
else:
    print("Pushover user not found")

if pushover_token:
    if pushover_token.startswith("a"):
        print("Pushover token found and looks good")
    else:
        print("Pushover token found but doesn't start with a")
else:
    print("Pushover token not found")


# the push function to send a message to pushover
def push(message):
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)


# TOOL 1
# The push_tool function is a tool that can be used by the agent to send a push notification to the user. 
# It is decorated with @function_tool so that it can be used as a tool in the agent's instructions. 
# The function takes a message as input and sends it to the user via the Pushover API. 
# It returns a string indicating the status of the API call.
@function_tool
def push_tool(message: str) -> str:
    """ Send the given message to the user as a push notification """
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    result = requests.post(pushover_url, data=payload).status_code
    return f"Push sent with API status code {result}"

print(push_tool)
print(push_tool.description)


# Notifier Agent
# The notifier agent is an agent that can be used to notify the user upon request.
notifier = Agent(name="Notifier", model="gpt-5.4-mini", instructions="You notify the user upon request", tools=[push_tool])

async def notify_pizza_arrival():
    with trace("Pizza has arrived"):
        return await Runner.run(notifier, "Notify the user that the pizza is here")


result = asyncio.run(notify_pizza_arrival())
print(result.final_output)


## Sessions (memory - short term memory)

# Agent without memory: demo
agent = Agent(name="Assistant", model="gpt-5.4-mini")

async def run_without_memory():
    response = await Runner.run(agent, "Hi there. My name is Steve.")
    print(response.final_output)

    response = await Runner.run(agent, "What's my name?")
    print(response.final_output)


asyncio.run(run_without_memory())


# Approach 1: Conversation list of dictionaries
# The conversation is a list of dictionaries, where each dictionary represents a message in the conversation.
async def run_with_conversation_list():
    response = await Runner.run(agent, "Hi there. My name is Steve.")
    print(response.final_output)

    print(response.to_input_list())

    next_input = response.to_input_list() + [{"role": "user", "content": "What's my name?"}]
    print(next_input)

    response = await Runner.run(agent, next_input)
    print(response.final_output)


asyncio.run(run_with_conversation_list())

# Approach 2: SQLiteSession
# The SQLiteSession is a session that stores the conversation in a SQLite database.
async def run_with_sqlite_session():
    # This is created in-memory
    # For an on-disk memory, use SQLiteSession("12345", "memory.db")

    session = SQLiteSession("12346") # 12346 is the session id (conversation thread id), which can be any string
    response = await Runner.run(agent, "Hi there. My name is Steve.", session=session)
    print(response.final_output)

    response = await Runner.run(agent, "What's my name?", session=session)
    print(response.final_output)