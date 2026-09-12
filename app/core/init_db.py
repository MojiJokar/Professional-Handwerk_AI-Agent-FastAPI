# from app.core.database import engine
# from app.models.customer import Base


# async def init_db():

#     async with engine.begin() as conn:

#         await conn.run_sync(
#             Base.metadata.create_all
#         )


#===============================================The last one which worked properlly is following:
# from app.core.database import engine


# async def init_db():
#     print("DATABASE: testing connection...")

#     try:
#         async with engine.begin() as conn:
#             await conn.run_sync(lambda connection: None)

#         print("DATABASE: connection successful!")

#     except Exception as e:
#         print(f"DATABASE: connection failed!")
#         print(f"ERROR: {e}")
#         raise
    
#     # to test: $ fastapi dev app/main.py

# for security we use followoing :
from app.core.database import engine

from app.models.customer import Base
from app.models.user import User


async def init_db():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

























# db connection Test 2==================================
# from fastapi import FastAPI
# from sqlalchemy import text

# from app.core.database import engine

# app = FastAPI()


# @app.get("/db-test")
# async def db_test():
#     try:
#         async with engine.connect() as connection:
#             result = await connection.execute(text("SELECT 1"))
#             value = result.scalar()

#         return {
#             "database": "connected",
#             "test": value
#         }

#     except Exception as e:
#         return {
#             "database": "failed",
#             "error": str(e)
#         }
#++++++++++++++++++++++++++++++++++
# from sqlalchemy import text
# from app.core.database import engine


# async def init_db():
#     print("DATABASE: testing connection...")

#     try:
#         async with engine.begin() as conn:
#             result = await conn.execute(text("SELECT 1"))
#             print(f"DATABASE: query result = {result.scalar()}")

#         print("DATABASE: connection successful!")

#     except Exception as e:
#         print("DATABASE: connection failed!")
#         print(f"ERROR: {e}")
#         raise

#test db
# from sqlalchemy import text
# from app.core.database import engine


# async def init_db():
#     print("DATABASE: testing connection...")

#     try:
#         async with engine.connect() as conn:
#             result = await conn.execute(text("SELECT 1"))
#             print(f"DATABASE TEST RESULT: {result.scalar()}")
#             print("DATABASE: connection successful!")

#     except Exception as e:
#         print("DATABASE: connection failed!")
#         print(f"ERROR TYPE: {type(e).__name__}")
#         print(f"ERROR: {e}")
#         raise
