from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field

router = APIRouter(prefix="/students",tags=["Students"])

students = [
    {"id": 1, "name": "Ali", "cgpa": 3.5},
    {"id": 2, "name": "Ahmed", "cgpa": 3.8}
]


class Student(BaseModel):
    id : int  = Field(gt=0,description="Enter Student ID")
    name : str = Field(min_length=3, description="Enter Student Name")
    cgpa : float = Field(ge=0,le=4, description="Enter CGPA")


class StudentUpdate(BaseModel):
    name : str = Field(min_length=3)
    cgpa : float = Field(ge=0,le=4)

def check_login():
    print("Checking login....")

@router.post("/",status_code=201,summary="Create a new student",deprecated=True,responses={
    409:{"description" : "Student with this ID already exists"}
})
def create_student(new_student:Student, user = Depends(check_login)):

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

@router.get("/")
def get_students(user=Depends(check_login)):
    return students

@router.get("/{id}",responses={
    404:{
        "description":"Student not found"
        }
}
)
def get_student(id:int,user=Depends(check_login)):
    for student in students:
        if student["id"]==id:
            return student
        
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

#Just a practice
@router.put("/{id}",responses={
    404:{"description":"Student not found"}
})
def update_student(id : int, updated_student:StudentUpdate,user=Depends(check_login)):
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


@router.delete("/{id}",responses={
    404 : {
        "message":"Student deleted successfully"
    }
})
def delete_student(id : int, user=Depends(check_login)):
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
