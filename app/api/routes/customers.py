from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
)
from app.services.customer_service import CustomerService


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


service = CustomerService()


@router.post(
    "/",
    response_model=CustomerResponse
)
async def create_customer(
    data: CustomerCreate,
    db: Annotated[
        AsyncSession,
        Depends(get_db)
    ],
):

    return await service.create(
        db,
        data
    )