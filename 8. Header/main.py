from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()

# creating for handling the custom header tag are sending
# Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-)
# But a variable like user-agent is invalid in Python.
# so by default it will convert those hypen sign to underscore
@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}