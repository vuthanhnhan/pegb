from app.utils.database import Database
from .type import * 

class CategoryModel(Database):
    def __init__(self) -> None:
        super().__init__('category')