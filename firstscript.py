#  this is the first FastAPI script that I wrote
#  this is so amazing
#  for running this script i neet to install FastAPI and ASGI server named Uvicorn
#  pip3 install fastapi
#  pip3 install "uvicorn[standard]"
#  python3 -m uvicorn firstscript:app --reload 



from typing import Union 
from fastapi import FastAPI 
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello", "World", "!", "..."}


@app.get("/items/{item_id}")
def read_item(item_id:int, q:Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/new_item/{item_id}")
def add_new_item(item_id:int, item:Item):
    return {
        item_id,
        item.name,
        item.price,
    }
