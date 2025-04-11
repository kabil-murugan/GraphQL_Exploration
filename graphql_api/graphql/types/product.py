"""Object type for Product."""

import strawberry


@strawberry.type
class Product:
    """Product Object Type."""

    id: strawberry.ID
    name: str
    price: float
