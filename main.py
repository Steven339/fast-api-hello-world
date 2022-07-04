from typing import Dict, Optional

from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    email: str
    password: str
    cellphone: Optional[str]


class Location(BaseModel):
    city: str
    state: str
    country: str
    address: str


@app.get("/")
def home(string) -> Dict:
    """Home API"""
    return {"success": True, "string": string}


@app.post("/user/create")
def user_create(user: User = Body(...)):
    return user


@app.get('/user/detail')
def user_detail(
        email: str = Query(
            min_length=5,
            max_length=50,
            title="User email",
            description="This is the user email. It's between 5 and 50 characters."
        ),
        password: str = Query(
            ...,
            min_length=6,
            title="User password",
            description="This is the user password. Min 6 characters"
        ),
        cellphone: Optional[str] = Query(
            None,
            min_length=10,
            max_length=10,
            title="User cellphone",
            description="This is the user password. Min 10 characters"
        )
):
    return {
        "email": email,
        "password": password,
        "cellphone": cellphone
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
        user_id: int = Path(
            ...,
            title="User id",
            description="This is the user id field",
            gt=0
        ),
        user: User = Body(...),
        location: Location = Body(...)
):
    results = user.dict()
    results.update(location.dict())
    return results
