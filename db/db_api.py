import logging
from typing import Union

import aiomysql
from aiomysql import Pool

from models.models import BookModel, UserModel
from .db_models import *


class DbApi:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await aiomysql.create_pool(
            user='root',
            password='bobdev2004',
            host='localhost',
            db='library',
            pool_recycle=3600,
            port=3306,
            autocommit=True
        )

    async def execute_cmd(self, command, *args,
                          fetch: bool = False,
                          fetchval: bool = False,
                          fetchrow: bool = False,
                          execute: bool = False
                          ):
        async with self.pool.acquire() as connection:
            try:
                async with connection.cursor() as cursor:
                    await cursor.execute(command, *args)
                    if fetch:
                        result = await cursor.fetchall()
                    elif fetchval:
                        result = await cursor.fetchone()[0]
                    elif fetchrow:
                        result = await cursor.fetchone()
                    elif execute:
                        # result = await connection.execute(command, *args)
                        result = True
                        # result = await cursor.execute(command, *args)

                return result
            except Exception as e:
                logging.error(e)
                return False

    async def close(self):
        self.pool.close()
        await self.pool.wait_closed()

    """
    user table functions
    """

    async def get_user(self, user_id: int):
        res = await self.execute_cmd("select * from User where user_id = %s", user_id, fetchrow=True)
        return User(**dict(zip(User.__fields__.keys(), res))) if res else None

    async def get_users(self):
        res = await self.execute_cmd("select * from User", fetch=True)
        return [User(**dict(zip(User.__fields__.keys(), user))) for user in res]

    async def add_user(self, user: UserModel):

        command = "insert into User values (null,%s, %s, %s, %s, %s)"

        res = await self.execute_cmd(command,
                                     (user.first_name, user.last_name, user.mail, user.address, user.phone),
                                     execute=True)

        return res

    """CATEGORY TABLE FUNCTIONS"""

    async def get_categories(self):
        res = await self.execute_cmd("select * from Category", fetch=True)
        return [Category(**dict(zip(Category.__fields__.keys(), category))) for category in res]

    """BOOK TABLE FUNCTIONS"""

    async def get_book(self, book_id: int):

        try:
            res = await self.execute_cmd("select * from Book where book_id = %s", book_id, fetchrow=True)
            return Book(**dict(zip(Book.__fields__.keys(), res))) if res else None
        except Exception as e:
            logging.error(e)
            return None




    async def get_books(self):
        res = await self.execute_cmd("select * from Book", fetch=True)
        return [Book(**dict(zip(Book.__fields__.keys(), book))) for book in res]




    async def add_book(self, book: BookModel, author_id: int):
        command = "insert into Book values (null,%s, %s, %s, %s, %s, %s, %s)"

        res = await self.execute_cmd(command,
                                     (book.title, book.number_of_pages, book.status, book.language_id, book.category_id,
                                      book.ISBN),
                                     book.dict(exclude_unset=True),
                                     execute=True)

        return res
