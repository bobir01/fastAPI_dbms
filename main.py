from fastapi import FastAPI, Response

from db import DbApi
from models.models import CategoryModel, UserModel, BookModel

app = FastAPI()
db = DbApi()


@app.on_event("startup")
async def startup():
    await db.create()


@app.get("/get_user", tags=["User"], response_model=UserModel)
async def get_user(user_id: int):
    """
    get user by `user_id`

    :**param** user_id:

    :**return**: User or 404


    """

    res = await db.get_user(user_id)

    return Response(content='User not found', status_code=404) if not res else res


@app.get("/get_users", tags=["User"], response_model=list[UserModel])
async def get_users():
    """
    get all users

    :**return**: list of users

        """
    db_users: list[UserModel] = await db.get_users()
    return db_users


@app.post("/add_user", tags=["User"], responses={200: {"ok": True, "message": "user added"}}, status_code=200)
async def add_user(user: UserModel):
    """
    use this to add user

    :**param** user object:

    :**return**: {
                    message: "user added"
                    ok: True
                }

    """
    res = await db.add_user(user)
    return {"message": "user added", "ok": True} if res else {"message": "user not added", "ok": False}


@app.get("/get_categories", tags=["Category"], response_model=list[CategoryModel])
async def get_categories():
    """
    get all categories

    :**return**: list of categories

    """
    db_categories: list[CategoryModel] = await db.get_categories()
    return db_categories


@app.get("/get_book", tags=["Book"], response_model=BookModel)
async def get_book(book_id: int):
    """
    get book by `book_id`

    :**param** book_id:

    :**return**: Book or 404

    """
    res = await db.get_book(book_id)

    return Response(content='Book not found', status_code=404) if not res else res



@app.get("/get_books", tags=["Book"], response_model=list[BookModel])
async def get_books():
    """
    get all books

    :**return**: list of books

    """
    db_books: list[BookModel] = await db.get_books()
    return db_books
