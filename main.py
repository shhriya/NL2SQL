import os
import json
from dotenv import load_dotenv
from utils.gemini_client import get_sql_from_question
from utils.bigquery_client import run_query
from utils.memory import update_memory, get_memory_history

load_dotenv()
def build_prompt(question):
    with open("prompts/system_prompt.txt") as f:
        system_prompt = f.read()

    with open("metadata/spotify_metadata.json") as meta_file:
        metadata_json = json.load(meta_file)
        table_name = metadata_json.get("table_name", "spotify_2023")
        columns = metadata_json["columns"]
        metadata_str = "\n".join([f"- {col['name']} ({col['type']}): {col['description']}" for col in columns]) # for readable format for the llm

    full_prompt = (
        f"{system_prompt}\n\n"
        f"Table name: {table_name}\n"
        f"Table columns and descriptions:\n{metadata_str}\n\n"
        f"{get_memory_history()}\n\n"
        f"Q: {question}\nWhat is the query and answer?"
    )
    return full_prompt    

def summarize_answer(question, result):
    if not result:
        return "No results found."
    rows_preview = result[0:]
    table_summary = "\n".join([str(row) for row in rows_preview])
    summary_prompt = f"""You are a helpful assistant. Based on the SQL result below, answer the user’s question naturally.
Question: {question}
Result Preview:
{table_summary}
Answer:"""
    return get_sql_from_question(summary_prompt)
    
def main():
    while True:
        user_input = input("\n Ask me anything about Spotify dataset: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        prompt = build_prompt(user_input)
        response = get_sql_from_question(prompt)

        # Extract SQL from response
        sql_start = response.find("SELECT")
        sql = response[sql_start:].split("```")[0].strip()

        print("\n SQL Generated:")
        print(sql)

        if not sql.strip().lower().startswith("select"):
            print(" Query blocked! Only SELECT statements are allowed.")
            update_memory(user_input, sql, "Blocked non-SELECT query.")
            continue

        try:
            result = run_query(sql)
            natural_answer=summarize_answer(user_input,result)
            print("\nNatural language result: ",natural_answer)
            print("\nRaw Result:", result)
            update_memory(user_input, sql, str(result))
        except Exception as e:
            print(" Query failed:", e)

if __name__ == "__main__":
    main()
