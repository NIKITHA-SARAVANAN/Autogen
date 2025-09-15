from agents.problem_solver import get_problem_solver_agent
from agents.code_executor_agent import get_code_executor_Agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination 
from config.constant import MAX_TURNS
from config.constant import TEXT_MENTION
def get_dsa_team_and_local():
    problem_solver_agent=get_problem_solver_agent()
    code_executor_agent,local=get_code_executor_Agent()
    termination_condition=TextMentionTermination(TEXT_MENTION)
    team=RoundRobinGroupChat(
        participants=[
            problem_solver_agent,
            code_executor_agent,
        ],
        termination_condition=termination_condition,
        max_turns=MAX_TURNS
    )
    return team,local