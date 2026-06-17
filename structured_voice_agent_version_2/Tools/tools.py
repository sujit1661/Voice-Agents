from datetime import datetime
from langchain_core.tools import tool

@tool(description="used to get time")
def get_time():
    return datetime.now().strftime("%H:%M:%S")

@tool(description="used to get math calculation")
def calculator(expression: str):
    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {e}"
