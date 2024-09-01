from http import HTTPStatus

from fastapi import FastAPI

from fast_demo.routers import auth, todo, users
from fast_demo.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todo.router)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> dict:
    return {"message": "Hello fucking world!"}
