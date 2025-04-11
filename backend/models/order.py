"""Order models."""

from enum import Enum
from typing import List

from beanie import Document
from pydantic import BaseModel


class OrderStatus(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class OrderItem(BaseModel):
    product_id: str
    quantity: int


class Order(Document):
    user_id: str
    items: List[OrderItem]
    status: OrderStatus

    class Settings:
        name = "orders"
