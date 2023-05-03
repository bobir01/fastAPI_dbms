from decimal import Decimal as decimal
from typing import Optional

from pydantic import BaseModel
from pydantic.types import Enum


class StatusEnum(str, Enum):
    status_1 = "1"
    status_2 = "2"
    status_3 = "3"
    status_4 = "4"
    status_5 = "5"


class User(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    mail: str
    address: str
    phone: decimal


class Category(BaseModel):
    category_id: Optional[int]
    name: str


class Language(BaseModel):
    language_id: Optional[int]
    name: str


class Book(BaseModel):
    book_id: Optional[int]
    title: str
    number_of_pages: decimal
    status: StatusEnum
    category_id: int
    language_id: int
    cover_image: str
    ISBN: str

class Rented_books(BaseModel):
    book_id: Optional[int]
    user_id: int
    book_id: int
    rental_date: str
    return_date: str

class Returned_books(BaseModel):
    book_id: Optional[int]
    user_id: int
    book_id: int
    date: str
    return_date: str
    comment: str
    status: StatusEnum


class Author(BaseModel):
    author_id: Optional[int]
    first_name: str
    last_name: str


