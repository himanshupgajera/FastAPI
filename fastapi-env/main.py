from fastapi import FastAPI

app = FastAPI()

# simple route
@app.get("/")
async def root():
	return {"message": "Hello World"}

# route with parameters
@app.get("/items")
async def read_item():
	return {"message": "Items"}

# route with id parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
	return {"message": "Item ID: {}".format(item_id)}

# route with query parameters
@app.get("/items/{item_id}/{name}")
async def read_item_name(item_id: int, name: str):
	return {"message": [{"item_id": item_id, "name": name},{"item_id": item_id, "name": name}]}