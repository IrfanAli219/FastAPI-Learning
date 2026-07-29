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