def calculator_tool_function(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Error in calculation: {str(e)}"