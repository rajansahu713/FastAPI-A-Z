<h1 align='center'> FastAPI </h1>

Table of content
1. Introduction
2. Hello World API
3. 


<h2>Introductions</h2>

> FastAPI is a modern, python-based high-performance web framework used to create Rest APIs. Its key features are that is fast, up to 300% faster to code, fewer bugs, easy to use, and production-friendly.
 
<br>
FastAPI's Features

* Very high performance, on par with NodeJS and Go
* Increase the speed to develop features by about 200% to 300%
* Designed to be easy to use and learn. Less time reading docs
* Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs
* Get production-ready code. With automatic interactive documentation
<br><br>
<h3>FastAPI Alternatives & Comparisons</h3>

1. Flask
Flask is intended for getting started very quickly and was developed with best intentions in mind.
2. Django REST framework
It is a powerful and flexible toolkit that makes it easy to build Web APIs.

<h2>Hello World API</h2>

```python
# import package
from fastapi import FastAPI

# create instance of FastAPI
app = FastAPI()

# route
@app.get("/")
def read_root():
    return {"Hello": "World"}
```
save the file main.py
```python
uvicorn main:app --reload 
```
