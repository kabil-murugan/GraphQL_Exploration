from typing import List, Optional

import strawberry

from graphql_api.models.product import Product


async def get_products(fields: List[str]) -> List[Product]:
    """Fetch all products."""
    projection = {field: 1 for field in fields}
    return await Product.find_all(projection=projection).to_list()


async def get_product(
    id: strawberry.ID, fields: List[str]
) -> Optional[Product]:
    """Fetch a product by ID."""
    projection = {field: 1 for field in fields}
    product = await Product.get(id, projection=projection)
    if product:
        return product
    return None
