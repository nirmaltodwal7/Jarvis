from openai import OpenAI
# client = OpenAI()


client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant."},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)
print(completion.choices[0].message.content)
# import time
# import openai

# def make_request():
#     retries = 3
#     for i in range(retries):
#         try:
#             completion = openai.ChatCompletion.create(
#                 model="gpt-4",
#                 messages=[
#                     {"role": "user", "content": "Hello!"}
#                 ]
#             )
#             return completion
#         except openai.error.RateLimitError:
#             if i < retries - 1:
#                 print(f"Rate limit exceeded. Retrying in {2 ** i} seconds...")
#                 time.sleep(2 ** i)
#             else:
#                 raise

# # Call the function
# response = make_request()
