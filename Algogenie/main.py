import asyncio
import sys
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import asyncio
from teams.dsa_team import get_dsa_team_and_local
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from config.local_executor import get_local_executor

async def main():
    local=get_local_executor()
    dsa_team,local=get_dsa_team_and_local()
    try:
        task="write a python code to add two numbers"
        async for message in dsa_team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print('=='*20)
                print(message.source,":",message.content)
            elif isinstance(message,TaskResult):
                print('Stop Reason:',message.stop_reason)
                      
    except Exception as e:
        print("Error:{e}")
if __name__=="__main__":
    asyncio.run(main())   