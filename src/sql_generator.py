def generate_sql(question):
    """
    Converts natural language questions to SQL.
    Placeholder implementation.
    """

    if "sales" in question.lower():
        return "SELECT * FROM sales_promotions;"

    return "SELECT * FROM sales_promotions LIMIT 10;"
