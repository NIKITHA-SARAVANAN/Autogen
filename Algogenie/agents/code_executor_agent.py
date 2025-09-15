from autogen_agentchat.agents import CodeExecutorAgent
from config.local_executor import get_local_executor

def get_code_executor_Agent():
    """
    Function to get the code executor agent.
    This agent is responsible for executing code.
    It will work with the problem solver agent to execute the code.
    """
    local=get_local_executor()
    code_executor_agent=CodeExecutorAgent(name='CodeExecutorAgent',
                                            code_executor=local)
    return code_executor_agent,local