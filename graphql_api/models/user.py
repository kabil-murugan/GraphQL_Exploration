"""User models."""

from beanie import Document
from pydantic import BaseModel


class Profile(BaseModel):
    """Profile model for user information."""

    age: int
    location: str


class User(Document):
    """User model for the database."""

    name: str
    email: str
    profile: Profile

    class Settings:
        name = "users"
