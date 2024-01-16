import aiomysql
import os
from fastapi import HTTPException

class Database():
    def __init__(self) -> None:
        self.db_config = {
            "host": os.getenv("MYSQL_HOST"),
            "port": 3306,
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "db": os.getenv("MYSQL_DATABASE"),
            "autocommit": True,
        }

    async def operation(self, query, values=None):
        try:
            async with aiomysql.create_pool(**self.db_config) as pool:
                async with pool.acquire() as connection:
                    async with connection.cursor() as cursor:
                        await cursor.execute(query, values)
                        return cursor.fetchall()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database operation error: {str(e)}")
