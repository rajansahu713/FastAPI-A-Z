from fastapi import FastAPI

app = FastAPI()

items = {
        1:
            {"Name": "Rohit", "Age": "21","Address":"Pune"},
        2:
            {"Name": "Sonali", "Age": "22","Address":"Utter Pradesh"}
        }   

@app.get("/users/")
async def read_item(id: int):
    return items[id]