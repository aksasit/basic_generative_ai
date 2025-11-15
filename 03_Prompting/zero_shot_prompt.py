from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = '''You should only and only answer the coding related questions. Do not answer anything else.
Your name is Alexa. If user asks something other than coding, just say Sorry!'''

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user","content":"Write a code to answer the sum of two numbers"}
    ]
)

print(response.choices[0].message.content)