from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

data = {}

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

# Add a new blog
@app.post("/blog")
def create_blog(blog: Blog):
    data.append(blog)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog (id, title, description) VALUES (%s, %s, %s)", (blog.id, blog.title, blog.description))
    conn.commit()
    cursor.close()
    return blog

# Get all blogs
@app.get("/blog")
def get_blogs():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog")
    blogs = cursor.fetchall()
    cursor.close()
    if blogs is None:
        return {"Error":"No blog available"}
    else:
        return blogs

# Get a blog by id
@app.get("/blog/{id}")
def get_blog(id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog WHERE id = %s", (id,))
    blog = cursor.fetchone()
    cursor.close()
    if blog is None:
        return {"Error":"No blog available"}
    else:
        return blog

# Update a blog by id
@app.put("/blog/{id}")
def update_blog(id: int, blog: Blog):
    cursor = conn.cursor()
    cursor.execute("UPDATE blog SET title = %s, description = %s WHERE id = %s", (blog.title, blog.description, id))
    conn.commit()
    cursor.close()
    return {"Message":"Blog updated successfully"}

# Delete a blog by id
@app.delete("/blog/{id}")
def delete_blog(id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blog WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    return {"Message":"Blog deleted successfully"}