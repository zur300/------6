import os
import json
from openai import OpenAI
from pydantic import BaseModel

class Answer(BaseModel):
    answer: str
    confidence: float

client = OpenAI(
    base_url="https://api.anthropic.com/v1/",
    api_key = os.environ["ANTHROPIC_API_KEY"],
)

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages = [
        {"role": "system", "content": "Reply with ONLY a JSON object with two fields: 'answer' (a string) and 'confidence' (a number between 0 and 1). No other text, no markdown, no ```."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    temperature=0,
)

raw = response.choices[0].message.content
raw = raw.strip()                      # remove leading/trailing whitespace

# strip markdown code fences if the model added them
if raw.startswith("```"):
    raw = raw.strip("`")               # remove the backticks
    # after stripping backticks, there may be a leading "json" label
    if raw.startswith("json"):
        raw = raw[4:]
    raw = raw.strip()

    print(raw)
data = json.loads(raw)

print("answer", data["answer"])
print("confidence", data["confidence"]) 

result = Answer.model_validate_json(raw)
print("answer:", result.answer)
print("confidence:", result.confidence)
