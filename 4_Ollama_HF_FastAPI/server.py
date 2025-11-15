from fastapi import FastAPI, Body
from ollama import Client

app=FastAPI()
client=Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Message":"Hello World"}

@app.get("/contact-us")
def read_root():
    return {"Email":"aaalks125@gmail.com"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="Message to be recieved")
):
    response = client.chat(
        model="gemma2:2b",
        messages=[
            {
                "role":"user",
                "content":message
            }
        ]
    )
    
    return {"response": response.message.content}