from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

students = [
    {"id": 1, "name": "Ali", "cgpa": 3.5},
    {"id": 2, "name": "Ahmed", "cgpa": 3.8}
]

class Student(BaseModel):
    id : int  = Field(gt=0,description="Enter Student ID")
    name : str = Field(min_length=3, description="Enter Student Name")
    cgpa : float = Field(ge=0,le=4, description="Enter CGPA")


class StudentUpdate(BaseModel):
    name : str
    cgpa : float


@app.post("/students",status_code=201)
def create_student(new_student:Student):

    #Duplicate check
    for student in students:
        if student["id"] == new_student.id:
            raise HTTPException(
                status_code=409,
                detail="Student with this ID already exists"
            )
    #Conver pydantic object into dictionary
    student_data = new_student.model_dump()

    #Save into fake database
    students.append(student_data)

    #Return response
    return {
                "message" : "Student added successfully",
                "student":student_data
            }

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id:int):
    for student in students:
        if student["id"]==id:
            return student
        
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

#Just a practice
@app.put("/students/{id}")
def Update_student(id : int, updated_student:StudentUpdate):
    for student in students:
        if student["id"]==id:
            student["name"]=updated_student.name
            student["cgpa"]=updated_student.cgpa
            
            return {
                "Message":"Student updated successfully",
                "student" : student
            }

        
    raise HTTPException(
        status_code=404,
        detail="stuedent not found"
    )


@app.delete("/student/{id}")
def delete_student(id : int):
    for student in students:
        if id == student["id"]:
            students.remove(student)
            return {
                "message" : "Student deleted successfully"
            }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
