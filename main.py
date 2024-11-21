# Book resource
# implement CRUD endpoints on the book resource
# create user resource
# implement CRUD endpoints on the user resource

from fastapi import FastAPI
from routers.books import book_router
from routers.users import user_router

app = FastAPI()

app.include_router(book_router, prefix='/books', tags=["Books"])
app.include_router(user_router, prefix='/users', tags=["Users"])


@app.get("/")
def home():
    return {"message": "Welcome to bookapp!"}
