from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

data = []

db_name = "history"
db_user = "postgres"
db_pswd = "26082003"
db_host = "localhost"
db_port = "5432"

conn = psycopg2.connect(
    dbname = db_name,
    user = db_user,
    password = db_pswd,
    host = db_host,
    port = db_port
)

class Blog(BaseModel):
    id: int
    title: str
    description: str

@app.post("/blog")
def create_blog(blog: Blog):
    data.append(blog)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog (id, title, description) VALUES (%s, %s, %s)", (blog.id, blog.title, blog.description))
    conn.commit()
    cursor.close()
    return blog