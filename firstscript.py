#  this is the first FastAPI script that I wrote
#  this is a simple crud application
#  for running this script i neet to install FastAPI and ASGI server named Uvicorn
#  pip3 install fastapi
#  pip3 install "uvicorn[standard]"
#  python3 -m uvicorn firstscript:app --reload 



from typing import Union 
from fastapi import FastAPI 
from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    name: str
    price: int


class UpdateItem(BaseModel):
    name: str
    price: int


app = FastAPI()

api_prefix = "/items/apt/v1"

items: list = [
    {
        "item_id": 101,
        "name": "computer",
        "price": 1200,
    },
    {
        "item_id": 102,
        "name": "mobile",
        "price": 200,
    },
]


@app.get(api_prefix)
def get_items():
    return items


@app.get(api_prefix+"/{item_id}")
def get_one_item(item_id:int):
    for item in items:
        if item.get("item_id") == item_id:
            return item
    return {
        "msg": "no such item",
        "statusCode": 404
    }


@app.post(api_prefix)
def add_new_item(item:Item):
    items.append(
        {
            "item_id": item.item_id,
            "name": item.name,
            "price": item.price,
        }
    )
    return {
        "msg": "successfully add a new item",
        "statusCode": 201,
        "items": items
    }

@app.put(api_prefix+"{item_id}")
def update_item(item_id:int, updated_item:UpdateItem):

    for item in items:
        if item.get("item_id") == item_id:
            item["name"] = updated_item.name
            item["price"] = updated_item.price

            return {
                "msg": "successfully update item",
                "statusCode": 201,
                "items": items
            }

    return {
        "msg": "no such item",
        "statusCode": 404
    }


@app.delete(api_prefix+"{item_id}")
def delete_item(item_id:int):

    for item in items:
        if item.get("item_id") == item_id:
            items.remove(item)
            return {
                "msg": "successfully delete item",
                "statusCode": 201,
                "items": items
            }

    return {
        "msg": "no such item",
        "statusCode": 404
    }
