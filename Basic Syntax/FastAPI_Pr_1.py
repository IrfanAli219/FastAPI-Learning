from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def status():
    return {
        "status":"Running"
    }

@app.get("/students")
def students():
    return [{"id":1,"name":"Ali"},
            {"id":2,"name":"Ahmed"}]
students_data = students()
@app.get("/students/{id}")
def get_student(id:int):
    if id<=0:
        raise HTTPException(
            status_code=422,
            detail="id can only be positive"
        )
    for student in students_data:
        if student["id"]==id:
            return student
    raise HTTPException(
                status_code=404,
                detail="student not found"
        )

@app.get("/students/search")
def search(semester:int=6,department:str="CS"):
    return {"semester":semester,
            "department":department}

@app.get("/square/{number}")
def square(number:int):
    return {"square":number*number}

@app.get("/cube/{number}")
def cube(number:int):
    return {"cube":number*number*number}

@app.get("/calculator/divide")
def divide(a:int=20,b:int=5):
    if b==0:
        raise HTTPException(
            status_code=422,
            detail=f"can't be divided by {b}"
        )
    else:
        return {"result":a/b}

@app.post("/predict")
def prediction():
    return {"prediction":"Depression",
            "confidence":0.91}

@app.get("/weather")
def weather(weather:str):
    if weather=="cloudy":
        return "Cold"
    if weather=="sunny":
        return "warm"
