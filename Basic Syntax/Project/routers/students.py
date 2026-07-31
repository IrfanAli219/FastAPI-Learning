from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

students = [
    {"id": 1, "name": "Ali", "cgpa": 3.5},
    {"id": 2, "name": "Ahmed", "cgpa": 3.8}
]


# First Dependency
def check_login():
    print("Checking login...")

    return {
        "username": "Ali",
        "role": "admin"
    }


# Nested Dependency
def check_admin(user=Depends(check_login)):
    print("Checking admin...")

    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return user

class Student(BaseModel):
    id: int = Field(gt=0, description="Enter Student ID")
    name: str = Field(min_length=3, description="Enter Student Name")
    cgpa: float = Field(ge=0, le=4, description="Enter Student CGPA")


class StudentUpdate(BaseModel):
    name: str = Field(min_length=3)
    cgpa: float = Field(ge=0, le=4)

@router.post(
    "/",
    status_code=201,
    summary="Create a new student",
    deprecated=True,
    responses={
        409: {
            "description": "Student with this ID already exists"
        }
    }
)
def create_student(
    new_student: Student,
    user=Depends(check_login)
):
    # Duplicate Check
    for student in students:
        if student["id"] == new_student.id:
            raise HTTPException(
                status_code=409,
                detail="Student with this ID already exists"
            )

    student_data = new_student.model_dump()

    students.append(student_data)

    return {
        "message": "Student added successfully",
        "student": student_data
    }

@router.get("/")
def get_students(
    user=Depends(check_login)
):
    return students

@router.get(
    "/{id}",
    responses={
        404: {
            "description": "Student not found"
        }
    }
)
def get_student(
    id: int,
    user=Depends(check_login)
):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@router.put(
    "/{id}",
    responses={
        404: {
            "description": "Student not found"
        }
    }
)
def update_student(
    id: int,
    updated_student: StudentUpdate,
    user=Depends(check_login)
):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            student["cgpa"] = updated_student.cgpa

            return {
                "message": "Student updated successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@router.delete(
    "/{id}",
    responses={
        404: {
            "description": "Student not found"
        },
        403: {
            "description": "Access denied"
        }
    }
)
def delete_student(
    id: int,
    user=Depends(check_admin)
):
    for student in students:
        if student["id"] == id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )