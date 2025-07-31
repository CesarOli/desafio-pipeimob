from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str
    summary: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int