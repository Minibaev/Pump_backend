from typing import Union
from Pump_backend.main import app
from api.handlers import get_user_from_db, get_osts, add_user_in_db, add_ost_in_db


@app.post("/users/add/")
def add_user(name: str, surname: str, nickname: str, ost_id: int, email: str):
    add_user_in_db(name, surname, nickname, ost_id, email)
    return {"respones": "user create"}


@app.post("/ost/add/")
def add_user(neft_upr: str, ost: str):
    add_ost_in_db(neft_upr, ost)
    return {"respones": "ost create"}


@app.get("/users/{user_id}")
def get_user_id(user_id: int):
    res = get_user_from_db(user_id)
    return res


@app.get("/osts")
def update_item():
    res = get_osts()
    return res
