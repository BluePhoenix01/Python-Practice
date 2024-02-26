'''CRUD API'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class FruitModel(BaseModel):
    name: str
    color: str

fruits = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fruits/{name}", response_model=FruitModel)
def read_fruit(name: str):
    for fruit in fruits:
        if fruit.name == name:
            return fruit
    raise HTTPException(status_code=404, detail="Fruit not found")
@app.post("/fruits", response_model=FruitModel)
def create_fruit(fruit: FruitModel):
    for existing_fruit in fruits:
        if existing_fruit.name == fruit.name:
            raise HTTPException(status_code=400, detail="Fruit Exists")
    fruits.append(fruit)
    return fruit

@app.put("/fruits", response_model=FruitModel)
def edit_fruit(fruit: FruitModel):
    for existing_fruit in fruits:
        if existing_fruit.name == fruit.name:
            existing_fruit.color = fruit.color 
            return fruit
    raise HTTPException(status_code=404, detail="Fruit not found")

@app.delete("/fruits/{name}", response_model=FruitModel)
def del_fruit(name: str):
    for existing_fruit in fruits:
        if existing_fruit.name == name:
            fruits.remove(existing_fruit)
            return existing_fruit
    raise HTTPException(status_code=404, detail="Fruit not found")
