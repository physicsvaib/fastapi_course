import sqlite3
from .schemas import Shipment
from typing import Any


class Database:
    def __init__(self, table_name):
        self.db = sqlite3.connect("app/data/base.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        self.table_name = table_name

    def __del__(self):
        self.db.close()

    def create_table(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY,Content TEXT,Weight REAL,Status TEXT)",
        )

    def insert_data(self, data: Shipment) -> dict[str, Any] | None:
        self.cursor.execute(f"SELECT MAX(id) from {self.table_name}")
        res = self.cursor.fetchone()
        new_id = res[0] if res[0] is not None else 0
        new_id += 1

        self.cursor.execute(
            f"INSERT INTO {self.table_name} VALUES (?,?,?,?)",
            (new_id, data.content, data.weight, "placed"),
        )

        self.db.commit()

        self.cursor.execute(f"SELECT * from {self.table_name} where id = {new_id}")
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return {"id": row[0], "content": row[1], "weight": row[2], "status": row[3]}

    def get_data(self, id: int) -> dict[str, Any] | None:
        self.cursor.execute(f"SELECT * from {self.table_name} where id = {id}")

        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return {"id": row[0], "content": row[1], "weight": row[2], "status": row[3]}

    def delete_data(self, id: int):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = {id}")
        self.db.commit()

    def update_data(self, id: int, status: str):
        self.cursor.execute(
            f"UPDATE {self.table_name} SET Status = ? WHERE id = ?", (status, id)
        )

        self.db.commit()

        self.cursor.execute(f"SELECT * from {self.table_name} where id = {id}")
        row = self.cursor.fetchone()
        return {"id": row[0], "content": row[1], "weight": row[2], "status": row[3]}
