from typing import Optional

from pydantic import BaseModel
from pydantic.types import Enum


class StatusEnum(str, Enum):
    status_1 = "1"
    status_2 = "2"
    status_3 = "3"
    status_4 = "4"
    status_5 = "5"


class UserModel(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    mail: str
    phone: int
    address: str


class CategoryModel(BaseModel):
    category_id: Optional[int]
    name: str


class LanguageModel(BaseModel):
    language_id: Optional[int]
    name: str


class BookModel(BaseModel):
    book_id: Optional[int]
    title: str
    number_of_pages: int
    status: StatusEnum
    language_id: int
    category_id: Optional[int]
    cover_image: Optional[str]
    ISBN: str


class Rented_booksModel(BaseModel):
    book_id: Optional[int]
    user_id: int
    book_id: int
    rental_date: str
    return_date: str


class Returned_booksModel(BaseModel):
    book_id: Optional[int]
    user_id: int
    book_id: int
    date: str
    return_date: str
    comment: str
    status: StatusEnum
