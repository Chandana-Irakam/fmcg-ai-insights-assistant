# FMCG AI Insights Assistant

An AI-powered conversational analytics assistant for FMCG (Fast-Moving Consumer Goods) businesses. The system enables users to interact with sales and inventory data using natural language and receive business insights without requiring SQL knowledge or manual dashboard analysis.

---

## Problem Statement

Business teams frequently require insights regarding:

- Promotional performance
- Inventory movement
- Regional sales comparisons
- Product-level campaign effectiveness

Traditionally, these requests depend on analysts and dashboarding tools, causing delays and creating bottlenecks. This project explores how Large Language Models (LLMs) can automate analytical workflows through conversational interfaces.

---

## Features

- Natural language business queries
- Automatic query interpretation
- Sales performance summaries
- Inventory movement analysis
- Regional comparison reports
- Promotion effectiveness analysis
- Product-level campaign impact analysis
- Structured business insights generation

---

## Example Questions

Users can ask questions such as:

- Which region generated the highest revenue?
- How did promotions affect sales performance?
- Which products experienced stockouts?
- Compare sales across different regions.
- Which campaign produced the highest uplift?
- What was the total revenue during promotion weeks?

---

## System Architecture

```text
                    User Question
                           │
                           ▼
                Natural Language Query
                           │
                           ▼
                  SQL Generation Layer
                           │
                           ▼
                    Query Execution
                           │
                           ▼
                      Dataset / DB
                           │
                           ▼
                  Analytical Results
                           │
                           ▼
                Business-Friendly Response
```

---

## Tech Stack

### Backend

- Python

### Data Processing

- Pandas
- NumPy

### AI Layer

- LangChain
- Google Gemini / OpenAI

### Database

- SQLite
- PostgreSQL

### Frontend

- Streamlit

### Deployment

- Streamlit Cloud
- Render

---

## Project Structure

```text
fmcg-ai-insights-assistant
│
├── data/
│   ├── sales_promotions.csv
│   ├── inventory.csv
│   ├── product_master.csv
│   └── store_master.csv
│
├── src/
│   ├── app.py
│   ├── database.py
│   ├── sql_generator.py
│   ├── query_executor.py
│   ├── llm_chain.py
│   └── utils.py
│
├── prompts/
│   ├── system_prompt.txt
│   └── examples.txt
│
├── docs/
│   └── architecture.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset Design

The project uses four interconnected datasets:

### Sales & Promotions

Contains:

- Product ID
- Store ID
- Revenue
- Units Sold
- Promotion Type
- Discount Percentage
- Weekly sales records

### Inventory

Tracks:

- Opening stock
- Units received
- Units sold
- Closing stock
- Stockout events

### Product Master

Contains:

- Product name
- Brand
- Category
- Pack size
- Unit price

### Store Master

Contains:

- Region
- City
- Store format
- Store identifiers

---

## Edge Cases Incorporated

To simulate realistic FMCG behavior, the dataset includes:

### Demand Spikes

Promotions increase sales significantly.

### Stockouts

Popular products may run out of inventory.

### Regional Variations

Consumer demand differs across regions.

### Slow-Moving Products

Certain items exhibit low demand.

### Promotion-Free Weeks

Not all periods contain active campaigns.

### Uneven Campaign Performance

Promotions do not always improve revenue.

### Missing Replenishment Events

Some stores receive delayed inventory.

---

## Workflow

### Step 1

User submits a business question.

### Step 2

The system interprets the intent.

### Step 3

SQL queries are generated.

### Step 4

Relevant data is retrieved.

### Step 5

Results are transformed into business insights.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/fmcg-ai-insights-assistant.git

cd fmcg-ai-insights-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/app.py
```

---

## Sample Output

### User Query

```
Which region generated the highest revenue?
```

### Generated SQL

```sql
SELECT region,
SUM(revenue)
FROM sales
GROUP BY region;
```

### Response

```
The South region generated the highest revenue during the selected period.
```

---

## Challenges Faced

### SQL Hallucinations

The LLM occasionally generated invalid column names.

### Schema Alignment

Maintaining consistency across datasets required careful design.

### Query Accuracy

Business questions needed proper mapping to database operations.

### Data Quality

Synthetic datasets required realistic edge cases and relationships.

---

## Solutions

- Prompt engineering
- Schema-aware query generation
- Validation mechanisms
- Iterative testing
- Error handling and debugging

---

## Future Improvements

### Version 2.0

- Vector database integration
- Retrieval-Augmented Generation (RAG)
- Multi-agent architecture
- Interactive dashboards
- Real-time analytics
- Cloud deployment
- Authentication and user management

---

## Repository Status

🚧 Under Development

---

## Author

**Chandana Irakam**

B.E. Computer Science and Engineering (AIML)

Chaitanya Bharathi Institute of Technology

Hyderabad, India

GitHub: https://github.com/Chandana-Irakam

LinkedIn: https://linkedin.com/in/chandana-irakam

---

## License

MIT License
