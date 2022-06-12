import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Correct this to standard English:\n\nI tell you seven years ago.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)