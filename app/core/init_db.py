from app.core.database import engine
from app.models.customer import Base


async def init_db():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )