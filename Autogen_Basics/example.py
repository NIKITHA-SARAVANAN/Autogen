import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

#Initialise the openAI model client
openai_client=OpenAIChatCompletionClient(model="gpt-4o-mini",api_key=api_key)

#define the function
def reverse_string(text:str):
    return text[::-1]
#Register the custom function as a tool
reverse_tool=FunctionTool(reverse_string,description='A tool to reverse a string')

#create an agent with custom tool
agent=AssistantAgent(
    name="ReverseAgent",
    model_client=openai_client,
    system_message="You are a helpful assistant that can reverse text using the reverse_string tool",
    tools=[reverse_tool]
    
)
#define a task
task="Reverse the text 'Hello, how are you?'"

#run the agent
async def main():
    result=await agent.run(task=task)
    print(f"Agent Response:{result.messages[-1].content}")
if __name__=="__main__":
    asyncio.run(main())    
    