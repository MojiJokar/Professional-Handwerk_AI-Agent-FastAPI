from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine

app = FastAPI()


@app.get("/db-test")
async def db_test():
    try:
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT 1"))
            value = result.scalar()

        return {
            "database": "connected",
            "test": value
        }

    except Exception as e:
        return {
            "database": "failed",
            "error": str(e)
        }
        
# for test db type in Browser: $http://127.0.0.1:8000/db-test