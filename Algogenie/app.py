import asyncio
import sys
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import streamlit as st 
from teams.dsa_team import get_dsa_team_and_local
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio
st.title("AlgoGenie-our DSA Problem Solver")
st.write("welcome to algogenie,your personal dsa problem solver! here you can find solutions to various data structures and algorithm problems")
task=st.text_input("enter your DSA problem or question",value='write a function to add two numbers')
async def run(team,task):
    try:
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg:=f"{message.source}:{message.content}")
                yield msg
            elif isinstance(message,TaskResult):
                print(msg:=f"Stp reason:{message.stop_reason}")
                yield msg
        print("task completed")
    except Exception as e:
        print(f"Error:{e}")
        yield f"Error:{e}"
    
    
if st.button("Run"):
    st.write("Running the task")
    team,local=get_dsa_team_and_local()
    async def collect_messages():
        async for msg in run(team,task):
            if isinstance(msg,str):
                if msg.startswith("User:"):
                    with st.chat_message('user'):
                        st.markdown(msg)
                elif msg.startswith('DSA_Problem_Solver_Agent'):
                    with st.chat_message('assistant'):
                        st.markdown(msg)    
                elif msg.startswith('Code_Executor_Agent'):
                    with st.chat_message('assistant'):
                        st.markdown(msg)      
            elif isinstance(msg,TaskResult):
                st.markdown(f"Stop Reason:{msg.stop_reason}")
    asyncio.run(collect_messages())            
                
    
    