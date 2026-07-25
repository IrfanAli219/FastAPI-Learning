from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(numbers: Numbers):

    result = numbers.a + numbers.b

    return {
        "result": result
    }

import pydantic
print(pydantic.__version__)