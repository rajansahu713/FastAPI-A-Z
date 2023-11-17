from fastapi import FastAPI, Depends, Body
from typing import Union

app = FastAPI()

def query_extractor(q: Union[str, None] = None):
    return q

def query_or_body_extractor(
        q: str = Depends(query_extractor),
        last_query: Union[str, None] =Body(None),
        limit : int=Body(0)):
    if not q:
        return last_query
    return q


@app.post('/item')
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {'q_or_body': query_or_body}

    
