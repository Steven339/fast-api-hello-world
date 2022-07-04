from enum import Enum
from typing import Dict, Optional

from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class Country(Enum):
    colombia = "COP"
    venezuela = "VEN"


class User(BaseModel):
    email: EmailStr = Field(
        ...,
        title="User email",
        description="This is the user email. It's between 5 and 50 characters."
    )
    password: str = Field(
        ...,
        min_length=6,
        title="User password",
        description="This is the user password. Min 6 characters"
    )
    cellphone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=10,
        title="User cellphone",
        description="This is the user password. Min 10 characters"
    )


class Location(BaseModel):
    city: str = Field(...)
    state: str = Field(...)
    country: Country = Field(...)
    address: str = Field(...)


@app.get("/")
def home(string) -> Dict:
    """Home API"""
    return {"success": True, "string": string}


@app.post("/user/create")
def user_create(user: User = Body(...)):
    return user


@app.get('/user/detail')
def user_detail(user: User = Body(...)):
    return {
        "email": user.email,
        "password": user.password,
        "cellphone": user.cellphone
    }


@app.get("/user/detail/{user_id}")
def user_detail_by_id(
        user_id: int = Path(
            ...,
            gt=0
        )
):
    return {user_id: "It exists!"}


@app.put("/user/{user_id}")
def user_update(
        user: User = Body(...),
        location: Location = Body(...)
):
    results = user.dict()
    results.update(location.dict())
    return results
