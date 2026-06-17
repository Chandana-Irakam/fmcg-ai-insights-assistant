# FMCG AI Insights Assistant

def greet():
    print("Welcome to FMCG AI Insights Assistant!")

def process_query(query):
    """
    Placeholder function for natural language queries.
    """
    return f"Processing query: {query}"

def main():
    greet()

    while True:
        query = input("\nAsk a business question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        response = process_query(query)
        print(response)


if __name__ == "__main__":
    main()
