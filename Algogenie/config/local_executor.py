from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from config.constant import WORK_DIR,TIMEOUT
def get_local_executor():
    """
    Function to get the local code executor.
    This executor will run the code in a local executor
    """
    local_executor=LocalCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIMEOUT
    )
    return local_executor