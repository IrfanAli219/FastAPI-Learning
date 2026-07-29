from fastapi import FastAPI
from routers.students import router as student_router


app = FastAPI()

app.include_router(student_router)
