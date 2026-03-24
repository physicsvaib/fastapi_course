from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from custom.schemas import BaseBook, UpdateBook
from typing import Dict

app = FastAPI()


books_data: Dict[int, BaseBook] = {}


@app.get("/scalar", include_in_schema=False)
def scalar_api():
    return get_scalar_api_reference(openapi_url=app.openapi_url)


# @app.get("/books")
# def get_books():
#     pass


@app.post("/book")
def add_book(book: BaseBook):
    new_id = (max(books_data.keys()) if books_data else 0) + 1
    books_data[new_id] = book
    print(books_data)
    return {"id": new_id}


@app.get("/book")
def get_book_by_id(id: int):
    if id in books_data:
        return {f"{id}": books_data[id]}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the id u are here for doesn't exist",
        )


@app.patch("/book")
def patch_book(id: int, book: UpdateBook):
    if id not in books_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="IDK what are we talking about",
        )
    update = book.model_dump(exclude_unset=True)
    books_data[id] = books_data[id].model_copy(update=update)
    return books_data[id]


@app.delete("/book")
def delete_book(id: int):
    if id not in books_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="IDK what are we talking about",
        )

    del_book = books_data.pop(id)
    return f"deleted {del_book}"


@app.get("/books")
def get_book_ids():
    return f"keys: {[i for i in books_data.keys()]}"
