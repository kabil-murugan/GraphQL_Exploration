"""Object Types for Orders."""

from typing import TYPE_CHECKING, List

import strawberry

from graphql_api.models.order import OrderStatus

if TYPE_CHECKING:
    from graphql_api.graphql.types.user import User


@strawberry.type
class OrderItem:
    """Order Item Object Type."""

    product_id: strawberry.ID
    quantity: int


@strawberry.type
class Order:
    """Order Object Type."""

    id: strawberry.ID
    items: List["OrderItem"]
    status: OrderStatus
    user: "User"
