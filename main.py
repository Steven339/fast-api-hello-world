from typing import Dict, Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    email: str
    password: str
    cellphone: Optional[str]


@app.get("/")
def home(string) -> Dict:
    """Home API"""
    return {"success": True, "string": string}


@app.post("/user/create")
def user_create(user: User = Body(...)):
    return user
