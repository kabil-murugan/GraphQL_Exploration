"""Initialize the database connection and models."""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from graphql_api.core.config import settings
from graphql_api.models.order import Order
from graphql_api.models.product import Product
from graphql_api.models.user import User
from graphql_api.utils.logger import get_logger

logger = get_logger(__name__)


async def init_db():
    """Initialize the database connection and models."""
    client = AsyncIOMotorClient(settings.mongo_url)
    await init_beanie(
        database=client[settings.mongo_db],
        document_models=[User, Order, Product],
    )
    logger.info("Database initialized successfully.")
