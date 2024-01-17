import aiomysql
import os
from fastapi import HTTPException

class Database():
    def __init__(self, table) -> None:
        self.table = table
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
                    async with connection.cursor(aiomysql.DictCursor) as cursor:
                        await cursor.execute(query, values)
                        return await cursor.fetchall()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database operation error: {str(e)}")

    async def find_one_by(self, conditions):
        query = f"SELECT * FROM {self.table} WHERE "
        where_clause = ' AND '.join(f"{key} = %s" for key in conditions.keys())
        query += where_clause
        values = list(conditions.values())

        result = await self.operation(query, values)
        return result[0] if result else None

    async def find_by(self, conditions):
        query = f"SELECT * FROM {self.table} WHERE "
        where_clause = ' AND '.join(f"{key} = %s" for key in conditions.keys())
        query += where_clause
        values = list(conditions.values())

        result = await self.operation(query, values)
        return result

    async def find_one_by_id(self, id):
        return await self.find_one_by({ "id": id })

    async def find_all(self):
        query = f"SELECT * FROM {self.table}"

        result = await self.operation(query)
        return result

    async def update(self, conditions, new_data):
        query = f"UPDATE {self.table} SET "
        update_fields = ', '.join(f"{key} = %s" for key in new_data.keys())
        query += update_fields + " WHERE "
        where_clause = ' AND '.join(f"{key} = %s" for key in conditions.keys())
        query += where_clause
        values = list(new_data.values()) + list(conditions.values())

        await self.operation(query, values)

    async def update_by_id(self, id, new_data):
        await self.update({ "id": id }, new_data)

    async def create(self, data):
        query = f"INSERT INTO {self.table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s']*len(data))})"
        values = list(data.values())

        return await self.operation(query, values)

    async def delete_by_id(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        values = (id,)

        await self.operation(query, values)
