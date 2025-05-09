from fastapi import FastAPI
from app.endpoints import users
from app.db import engine
from app.models import users as user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])

user.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*"],              
)