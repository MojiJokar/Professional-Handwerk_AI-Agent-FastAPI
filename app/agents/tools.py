from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer


async def find_customer_by_email(
    db: AsyncSession,
    email: str
):

    result = await db.execute(
        select(Customer).where(
            Customer.email == email
        )
    )

    customer = result.scalar_one_or_none()

    if not customer:
        return None

    return {
        "id": customer.id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone,
        "city": customer.city,
    }
    
async def create_customer_tool(
    db: AsyncSession,
    name: str,
    email: str,
    phone: str | None,
    city: str | None
):

    customer = Customer(
        name=name,
        email=email,
        phone=phone,
        city=city,
    )

    db.add(customer)

    await db.commit()

    await db.refresh(customer)

    return {
        "id": customer.id,
        "name": customer.name,
        "email": customer.email,
    }