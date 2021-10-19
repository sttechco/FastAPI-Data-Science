from enum import Enum

from fastapi import FastAPI, Path, Body

from pydantic import BaseModel

app = FastAPI()

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

class User(BaseModel):
    name: str
    age: int

@app.get("/")
async def hello_world():
    return {"hello": "world"}

@app.get("/users/{id}")
async def get_user(id: int):
    return {"id": id}

# @app.get("/users/{type}/{id}/")
# async def get_user(type: str, id: int):
#     return {"type": type, "id": id}

@app.get("/users/{type}/{id}/")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
    return {"license": license}

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")): # http://127.0.0.1:8000/license-plates/AB-123-CD
    return {"license": license}

# @app.get("/users")
# async def get_user(page: int = 1, size: int = 10):
#     return {"page": page, "size": size}

# @app.get("/users")
# async def create_user(name: str = Body(...), age: int = Body(...)):
#     return {"name": name, "age": age}

@app.get("/users")
async def create_user(user: User):
    return user