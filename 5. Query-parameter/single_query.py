from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/users/{user_id}")
def read_main(user_id: str, q: Optional[str] = None):
    return {"user_id":{user_id}, "q": q}