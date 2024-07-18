import anthropic
from models.anthropic.sampler import Claude3SonnetSampler

s = Claude3SonnetSampler()
print(s([
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "hello"
                }
            ]
        }
    ]
))

# client = anthropic.Anthropic(
#     # defaults to os.environ.get("ANTHROPIC_API_KEY")
#     # api_key="my_api_key",
# )

# message = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0,
    # messages=
    # ]
# )
# print(message.content)