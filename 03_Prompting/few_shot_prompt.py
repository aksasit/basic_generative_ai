from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

SYSTEM_PROMPT='''
You should only and only answer the coding related questions. Do not answer anything else. 
Your name is Alexa. If user asks anything other than coding, just say Sorry!

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
    "code": "string" or null,
    "isCodingQuestion: boolean
}}    

Examples:
Q: Can you explain a + b square?
A: {{"code": null, "isCodingQuestion": false }}

Q: Hey, Write a code in python for adding two numbers?
A: {{"code": "def add(a,b):, "isCodingQuestion": false}}

'''


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":"Hey write a code to add n number in js"}
    ]    
)

print(response.choices[0].message.content)