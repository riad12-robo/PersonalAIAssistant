from openai import OpenAI
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)