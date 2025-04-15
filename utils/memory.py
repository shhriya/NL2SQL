memory = []

def update_memory(question, sql, answer):
    if len(memory) >= 3:
        memory.pop(0)
    memory.append({"question": question, "sql": sql, "answer": answer})

def get_memory_history():
    return "\n".join([f"Q: {m['question']}\nSQL: {m['sql']}\nA: {m['answer']}" for m in memory])
