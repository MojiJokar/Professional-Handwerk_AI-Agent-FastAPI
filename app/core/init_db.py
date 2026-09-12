# # from app.core.database import engine
# # from app.models.customer import Base


# # async def init_db():

# #     async with engine.begin() as conn:

# #         await conn.run_sync(
# #             Base.metadata.create_all
# #         )
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