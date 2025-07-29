from pydantic import BaseModel
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
    id: int

    class Config:
        orm_mode = True