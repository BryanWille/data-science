import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)
print(response)