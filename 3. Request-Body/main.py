from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class StudentDetails(BaseModel):
    roll_no: int
    name: str
    address: Optional[str] = None
    mark: float


app = FastAPI()


@app.post("/students/")
async def create_item(studentdetails: StudentDetails):
    return studentdetails