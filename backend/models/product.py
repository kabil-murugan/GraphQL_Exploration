"""Product models."""

from beanie import Document


class Product(Document):
    """Product model for the database."""

    name: str
    price: float

    class Settings:
        name = "products"
