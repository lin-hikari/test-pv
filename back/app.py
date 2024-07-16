from back.routers import users, complaints
from fastapi import FastAPI
from http import HTTPStatus
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(complaints.router)

@app.get('/', status_code=HTTPStatus.OK)  
def read_root():  
    return {'message': 'Olá Mundo!'}