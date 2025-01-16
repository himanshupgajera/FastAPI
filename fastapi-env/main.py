from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# simple route
@app.get("/")
async def root():
	return {"message": "Hello World"}

# route with parameters
@app.get("/items")
async def read_item():
	return {"items": "Items"}

# route with id parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
	return {"items": "Item ID: {}".format(item_id)}

# route with query parameters
@app.get("/items/{item_id}/{name}")
async def read_item_name(item_id: int, name: str):
	return {"items": [{"item_id": item_id, "name": name},{"item_id": item_id, "name": name}]}

# query for availabe and not aviailable items
@app.get("/items")
async def read_item_name(limit: int, available: bool):
	if available:
		return {"message":f'Available items: {limit}'}
	else:
		return {"message":f'Not available items: {limit}'}

# add a new item
@app.post("/products/{item_id}")
async def create_item(item_id: int):
	return {"items": f"Item ID: {item_id} added successfully"}

# add a new item with request body
class Item(BaseModel):
	name: str
	description: str
	price: float
	tax: float

@app.post("products/name")
async def add_name(item: Item):
	return {f"{item.name} added successfully"}
