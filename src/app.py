from database import load_sales_data
from sql_generator import generate_sql
from query_executor import execute_query
from llm_chain import generate_response


def main():
    sales_data = load_sales_data()

    if sales_data is None:
        print("Failed to load dataset.")
        return

    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        sql_query = generate_sql(question)
        result = execute_query(sql_query, sales_data)
        response = generate_response(question, result)

        print("\nGenerated SQL:")
        print(sql_query)

        print("\nResult:")
        print(result)

        print("\nAI Response:")
        print(response)


if __name__ == "__main__":
    main()
