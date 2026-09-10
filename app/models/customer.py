from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(200)
    )

    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )