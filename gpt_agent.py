# import openai

# class GPTAgent:
#     def __init__(self, api_key):
#         openai.api_key = api_key

#     def reply_to_issue(self, ctx):
#         prompt = f"""Issue in {ctx['repo']} by @{ctx['user']}:
# Title: {ctx['title']}
# Body: {ctx['body']}

# Please write a helpful, concise, and polite response."""
#         resp = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return resp.choices[0].message.content
from openai import OpenAI

class GPTAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def reply_to_issue(self, ctx):
        prompt = f"""Issue in {ctx['repo']} by @{ctx['user']}:
Title: {ctx['title']}
Body: {ctx['body']}

Please write a helpful, concise, and polite response."""
        
        resp = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
