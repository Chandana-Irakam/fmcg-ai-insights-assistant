def generate_sql(question):
    question = question.lower()

    if "revenue" in question:
        return "SELECT SUM(revenue) FROM sales"

    if "units sold" in question:
        return "SELECT SUM(units_sold) FROM sales"

    if "promotion" in question:
        return "SELECT * FROM sales WHERE promotion_flag = True"

    return "SELECT * FROM sales"
