from fastapi import FastAPI, Header
from typing import Union

app = FastAPI()

# so in the header we will mention user-id and we will received it as user_id
@app.get("/items/")
async def read_items(user_id: Union[str, None] = Header(default=None)):
    return {"User ID": user_id}