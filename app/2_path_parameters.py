from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(
    item_id: int,
):  # The parameter shoudl be integer like "http://127.0.0.1:8000/items/3"
    return {"item_id": item_id}


@app.get("/users/me")  # "me" path should be define in front of "user_id"
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")  # The second path doen't run
async def read_users2():
    return ["Bean", "Elfo"]


# Predefined values¶
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Path convertor
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


## Recap
# With FastAPI, by using short, intuitive and standard Python type declarations, you get:

# Editor support: error checks, autocompletion, etc.
# Data "parsing"
# Data validation
# API annotation and automatic documentation
