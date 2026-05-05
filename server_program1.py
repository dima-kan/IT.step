from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Response(BaseModel):
    message: str


@app.get("/greeting")
def greeting() -> Response:
    return Response(
        message="Привіт з сервера2",
    )
