from sqlalchemy.orm import Mapped

from .base import Base


class Order(Base):
    __tablename__ = "order"

    name: Mapped[str]
    price: Mapped[int]