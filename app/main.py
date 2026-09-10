# from fastapi import FastAPI


# app = FastAPI()


# @app.get("/")
# def home():
#     return {
#         "message": "AI Agent API is running"
#     }
# # Test .env use in main.py    
# from dotenv import load_dotenv
# import os


# load_dotenv()

# app_name = os.getenv("APP_NAME")

# print(app_name)
#==============================================Test over====

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_db()

    yield


app = FastAPI(
    title="AI Customer Agent",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():

    return {
        "message": "AI Agent API is running"
    }






