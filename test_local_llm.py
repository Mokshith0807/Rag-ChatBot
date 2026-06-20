from chains.local_llm import generate_local_answer, load_local_llm

print("Loading local model... (this may take 30-60 seconds)")

llm = load_local_llm()

print("Model loaded successfully!")

prompt = """
You are a helpful assistant.

Question:
What is artificial intelligence?

Answer:
"""

response = generate_local_answer(llm, prompt)

print("\nResponse:\n")
print(response)
