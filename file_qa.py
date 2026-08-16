import os
# import json
from openai import OpenAI
from pydantic import BaseModel

# class Answer(BaseModel):
#     answer: str
#     confidence: float

client = OpenAI(
    base_url="https://api.anthropic.com/v1/",
    api_key = os.environ["ANTHROPIC_API_KEY"],
)

path = input("File path: ")
with open(path, encoding="utf-8") as f:
    document = f.read()

question = input("Question: ")

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages = [
        {"role": "system", "content": " You are a helpful assistant.  i hand you a document, answer only using the provided document — do not use outside knowledge or guess. Quote the exact passage from the document that supports the answer (the reference). If the answer is not in the document, reply with a fixed sentence: \"Sorry, I can't find that in the document.\" and nothing else. answer in a string"},
        {"role": "user", "content": f"Document:\n{document}\n\nQuestion: {question}"},
    ],
    temperature=0,
)

raw = response.choices[0].message.content
print("answer: ", raw)
# raw = raw.strip()                      # remove leading/trailing whitespace

# strip markdown code fences if the model added them
# if raw.startswith("```"):
#     raw = raw.strip("`")               # remove the backticks
#     # after stripping backticks, there may be a leading "json" label
#     if raw.startswith("json"):
#         raw = raw[4:]
#     raw = raw.strip()

#     print(raw)
# data = json.loads(raw)


# print("answer", data["answer"])
# print("confidence", data["confidence"]) 

# result = Answer.model_validate_json(raw)
# print("answer:", result.answer)
# print("confidence:", result.confidence)
