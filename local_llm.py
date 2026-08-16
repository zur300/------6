from transformers import pipeline

pipe = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

messages = [
    {"role": "user", "content": "Give me a recipe for gluten-free pizza."},
]
result = pipe(messages, max_new_tokens=256)

# print(result[0]["generated_text"])
print(result[0]["generated_text"][-1]["content"])