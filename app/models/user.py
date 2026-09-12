from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.customer import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String(300),
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(500)
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )