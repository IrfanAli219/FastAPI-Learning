students = [
    {"id": 1, "name": "Ali", "cgpa": 3.5},
    {"id": 2, "name": "Ahmed", "cgpa": 3.8},
    {"id": 3, "name": "Sara", "cgpa": 3.9}
]


from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/students")
def get_student():
    return students

@app.get("/students/{id}")
def get_student(id : int):
    for student in students:
        if student["id"] == id:
            return student
        
    raise Exception(
                status_code = 404,
                detail = "Student not found"
            )