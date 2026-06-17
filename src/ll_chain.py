def generate_response(question, result):

    if isinstance(result, (int, float)):
        return f"The answer to '{question}' is {result}."

    return f"Retrieved {len(result)} records for '{question}'."
