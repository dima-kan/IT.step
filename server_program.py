from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# @app.get("/hello_world")
# def hello_world():
#     return {"message": "Hello World"}
#
#
# @app.post("/register/{username}")
# def register(username: str):
#     return {
#         "username": username,
#         "is_registered" : True
#     }
#
#
# data:dict [str,str]

# авдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер


# class Response(BaseModel):
#     message: str
#
# @app.post("/hello")
# def hello_world()->Response:
#     return Response(
#         message="Hello World"
#     )
#

# Завдання 2
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва
# сервери
# class Response(BaseModel):
#     message: str
#
# @app.get("/greeting")
# def greeting()-> Response:
#     return Response(
#          message="Привіт з сервера1",
#     )
#


class Book(BaseModel):
    id: int
    title: str
    autor: str
    year: int
    pages: int


@app.get("/books/")
def all_books() -> List[Book]:
    with open("books.json") as file:
        books = json.load(file)
        return books


@app.get("/books/{id}")
def get_book(id: int):
    with open("books.json") as file:
        books = json.load(file)

    for book in books:
        if book["id"] == id:
            return book


@app.post("/books/")
def create_book(book: Book) -> dict[str, str]:
    with open("books.json") as file:
        books = json.load(file)

    books.append(book.model_dump())

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)
    return {"message": "Книга додана успішно"}
