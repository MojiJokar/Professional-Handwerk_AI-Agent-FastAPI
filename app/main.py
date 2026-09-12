# # from fastapi import FastAPI


# # app = FastAPI()


# # @app.get("/")
# # def home():
# #     return {
# #         "message": "AI Agent API is running"
# #     }
# # # Test .env use in main.py    
# # from dotenv import load_dotenv
# # import os


# # load_dotenv()

# # app_name = os.getenv("APP_NAME")

# # print(app_name)
# #==============================================Test over====

from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.init_db import init_db
from app.api.routes.agent import router as agent_router
from app.api.routes.customers import router as customer_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("STARTUP: beginning")
    await init_db()
    yield
    print("SHUTDOWN: ending")


app = FastAPI(
    title="AI Customer Agent",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(agent_router)
app.include_router(customer_router)


@app.get("/")
async def root():
    return {
        "message": "AI Agent API is running"
    }



