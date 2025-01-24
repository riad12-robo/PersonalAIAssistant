import openai

openai.api_key = "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"

# Check if the key is valid and the models available
models = openai.Model.list()
for model in models["data"]:
    print(model["id"])
