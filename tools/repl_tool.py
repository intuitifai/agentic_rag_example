from io import StringIO
import contextlib

def repl_tool_function(code):
    try:
        # Try evaluating expressions
        result = eval(code)
        return result
    except SyntaxError:
        # If there's a SyntaxError, it's likely a code block that needs exec
        output = StringIO()
        with contextlib.redirect_stdout(output):
            try:
                exec(code)
                return output.getvalue().strip() or "Code executed without output."
            except Exception as e:
                return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
