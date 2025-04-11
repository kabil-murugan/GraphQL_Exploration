"""Object Types for User."""

from typing import TYPE_CHECKING, List

import strawberry

if TYPE_CHECKING:
    from graphql_api.graphql.types.order import Order


@strawberry.type
class Profile:
    """Profile Object Type."""

    age: int
    location: str


@strawberry.type
class User:
    """User Object Type."""

    id: strawberry.ID
    name: str
    email: str
    profile: Profile
    orders: List["Order"]
