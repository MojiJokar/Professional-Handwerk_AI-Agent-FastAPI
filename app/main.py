from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Agent API is running"
    }
# Test .env use in main.py    
from dotenv import load_dotenv
import os


load_dotenv()

app_name = os.getenv("APP_NAME")

print(app_name)