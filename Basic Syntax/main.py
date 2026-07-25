from fastapi import FastAPI
from fastapi import HTTPException
#Challenge 1
app = FastAPI()

@app.get("/")
def status():
    return {"status":"Running"}

#Challenge 2

@app.get("/about")
def about():
    return {"developer":"Irfan",
            "framework":"FastAPI"}

#challenge 3
@app.get("/hello/{name}")
def hello(name:str):
    return {"message":f"Hello {name}"}

#Challenge 4
@app.get("/square/{number}")
def square(number:int):
    return {"square":number*number}

#Challenge 5

@app.get("/cube/{number}")
def cube(number:int):
    return {"cube":number*number*number}

#Challenge 6
@app.get("/user/{age}")
def user(age:int):
    if age<0:
        raise HTTPException(
            status_code = 422,
            detail = "Negative age!"
        )
    else:
        return {"age":age}
    
#Challenge 7(sorry teacher. iska solution aap bata do agar maine ghalat likha hua ha to)
@app.get("/search")
def search(name:str="Ali",city:str="Lahore"):
    return {
        "name":name,
        "city":city
    }

#Challenge 8(iska bi asnwer aap bata do agar ghalat ha to)
@app.get("/student1")
def student1(name:str="Ali",semester:int=4,cgpa:float=3.2):
    return {
        "name":name,
        "semester":semester,
        "cgpa":cgpa
    }

#Challenge 9(iska bi bata dena)
@app.get("/student/{roll_no}")
def student(roll_no:int,semester:int=6,department:str="CS"):
    return {"roll_no":roll_no,
            "semester":semester,
            "department":department}

#Challenge 10
@app.post("/predict")
def predict():
    return {"prediction":"Depression",
            "confidence":0.91}
#Bonus 1
@app.get("/add")
def add(a=10,b=20):
    return {"result":a+b}

#Bonus 2
@app.get("/multiply/{x}/{y}")
def multiply(x:int,y:int):
    return {"result":x*y}

#Bonus 3
@app.get("/divide")
def divide(a:int=10,b:int=0):
    if b==0:
        raise HTTPException(
            status_code=422,
            detail = f"can't divide by {b}"
        )
    else:
        return {"result":a/b}
    
#Bonus 4
@app.get("/check_age/{age}")
def check_age(age:int):
    if age<0:
        raise HTTPException(
            status_code= 422,
            detail = "age can't be negative"
        )
    elif age<18:
        return {"status":"Minor"}
    else:
        return {"status":"Adult"}
    
