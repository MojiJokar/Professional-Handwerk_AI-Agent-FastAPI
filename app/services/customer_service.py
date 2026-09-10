from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate


class CustomerService:

    async def find_by_email(
        self,
        db: AsyncSession,
        email: str
    ):

        result = await db.execute(
            select(Customer).where(
                Customer.email == email
            )
        )

        return result.scalar_one_or_none()


    async def create(
        self,
        db: AsyncSession,
        data: CustomerCreate
    ):

        customer = Customer(
            name=data.name,
            email=data.email,
            phone=data.phone,
            city=data.city,
        )

        db.add(customer)

        await db.commit()

        await db.refresh(customer)

        return customer