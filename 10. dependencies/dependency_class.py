from fastapi import FastAPI, Depends
from typing import Union

app = FastAPI()


class CommonQueryParams:
    def __init__(self,item_id:int, q: Union[str, None] = None, skip: int = 0, limit: int=100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get('/')
async def read_items(commans: CommonQueryParams = Depends()):
# async def read_items(commans: CommonQueryParams = Depends(CommonQueryParams)):

    return commans