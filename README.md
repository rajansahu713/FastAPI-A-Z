<h2 align='center'> FastAPI </h2>
<hr>

Table of content
1. Introduction
2. Hello World API
3. Path/Query parameters
4. Request Body
5. Responses



<h2>Introductions</h2>

    FastAPI is a modern, python-based high-performance web framework used to create Rest APIs. Its key features are that is fast, up to 300% faster to code, fewer bugs, easy to use, and production-friendly.
 
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
* Save the file **main.py** run the below command

```python
uvicorn main:app --reload 
```
Open your browser at http://127.0.0.1:8000.

You will see the JSON response as:
```
{"message": "Hello World"}
```

* <h3>Path/Query Parameters</h3>

## 1. Path Parameter
```python
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
* You can declare the type of a path parameter in the function, using standard Python type

* **Path parameters with types**

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int)
```
* If you run this example and open your browser at http://127.0.0.1:8000/items/3, you will see a response of:

```json
{"item_id":3}
```
* But if you go to the browser at http://127.0.0.1:8000/items/foo, you will see a nice HTTP error

```json
{
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
}
```

* You can use the same type declarations with **str**, **float**, **bool** and many other complex data types.


## 2. Query Parameter

*  When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

```python
items = {
            1:
                {"Name": "Rohit", "Age": "21","Address":"Pune"},
            2:
                {"Name": "Sonali", "Age": "22","Address":"Utter Pradesh"}
        }   
@app.get("/users/")
async def read_item(id: int):
    return items[id]
```
* For example, in the URL:
 http://127.0.0.1:8000/users/?id=1

**Output**
```json
{"Name":"Rohit","Age":"21","Address":"Pune"}
```

* You can also define some parameter as default 
```python
from typing import Optional
from fastapi import FastAPI

app = FastAPI()
@app.get("/items/{username}")
async def read_user_item(
    username: str, marks: Optional[int] = None
):
    details = {"id": item_id, "marks": marks}
    return details
```
* In this case, there is 1 query parameters:

**username**, a required str.

**marks**, an optional int

## Request Body

* When you need to send data from a client to your API, you send it as a request body.
* A request body is data sent by the client to your API. A response body is the data your API sends to the client.
* Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

For request body we user pydantic

```python
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
```
* run the main.py file
```url
http://127.0.0.1:8000/students/
```
* request body
```json
{
    "roll_no":1,
    "name":"Sonal",
    "address":"Delhi",
    "mark":80
}
```

* With just that Python type declaration, FastAPI will:

    * Read the body of the request as JSON.
    * Convert the corresponding types (if needed).
    * Validate the data.
        * If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.



