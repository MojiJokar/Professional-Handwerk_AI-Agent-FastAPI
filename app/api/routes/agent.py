from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.agent import (
    EmailRequest,
    AgentResponse,
)


router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"]
)


@router.post(
    "/process-email",
    response_model=AgentResponse
)
async def process_email(
    request: EmailRequest,
    db: Annotated[
        AsyncSession,
        Depends(get_db)
    ],
):

    # Agent logic goes here

    return {
        "action": "human_review",
        "customer_id": None,
        "response": "Email received."
    }