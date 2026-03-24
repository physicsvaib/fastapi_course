from pydantic import BaseModel, Field
from typing import Any, Optional


class BaseBook(BaseModel):
    name_of_book: str = Field(default="", description="Name")
    author_name: str = Field(default="", description="Name of Author")
    edition: int = Field(default=1, description="What edition are we working with")
    pages: int = Field(default=0, description="Total Number of pages")


class UpdateBook(BaseModel):
    author_name: Optional[str] = None
    edition: Optional[int] = None
    pages: Optional[int] = None


class Book(BaseBook):
    id: int = Field(default=1)
