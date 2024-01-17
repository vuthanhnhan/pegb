from pydantic import BaseModel
from typing import Literal, Optional

class CategoryType(BaseModel):
    id: int
    name: str
    image: str
    discount: Optional[float]
