import os

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "system", "content": "你是一个经验丰富的、天马行空的、富有想象力的作家。"},
        {"role": "user", "content": "将子不语中的故事以一个主角的角度完成一篇小说，帮我列出大纲和大致情节。"},
    ],
    stream=False
)

print(response.choices[0].message.content)