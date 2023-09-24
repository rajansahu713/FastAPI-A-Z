from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class Details(BaseModel):
    title: str
    author: str

BOOKS ={
    '1':{"title":"Python for beginner", 'author': "abc"},
    '2':{"title":"JAVA for beginner", 'author': "xyz"},
    '3':{"title":"CPP for beginner", 'author': "aby"},
    '4':{"title":"Ruby for beginner", 'author': "auc"},
    '5':{"title":"SQL for beginner", 'author': "acc"},

}

@app.get('/books')
async def first_api():
    return {"data":BOOKS}

@app.post('/books')
async def first_api(details : Details):
    record = jsonable_encoder(details)
    BOOKS.update({f"{str(len(BOOKS)+1)}":record})
    return {"data":BOOKS}



@app.put('/books/{book_id}/')
async def first_api(book_id: int, details: Details):
    BOOKS[str(book_id)]= jsonable_encoder(details)
    return {"data":BOOKS}


@app.delete('/books/{book_id}/')
async def first_api(book_id: int):
    BOOKS.pop(str(book_id))
    return {"data":BOOKS}


