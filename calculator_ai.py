from byllm import Model

# Initialize the LLM (Python syntax)
llm = Model(model_name="gemini/gemini-2.0-flash", verbose=False)

def evaluate_expression(expression: str) -> str:
    """
    Evaluates a math expression and returns a string result.
    """
    try:
        # Simple arithmetic evaluator for testing
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"
