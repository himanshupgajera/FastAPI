from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post("/blog")
def create_blog(request: Blog):
    return f"Blog is created with title" + request.title