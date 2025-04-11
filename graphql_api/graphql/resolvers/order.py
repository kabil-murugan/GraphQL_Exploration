from typing import List, Optional

import strawberry

from graphql_api.models.order import Order


async def get_orders(fields: List[str]) -> List[Order]:
    """Fetch all orders."""
    projection = {field: 1 for field in fields}
    return await Order.find_all(projection=projection).to_list()


async def get_order(id: strawberry.ID, fields: List[str]) -> Optional[Order]:
    """Fetch a order by ID."""
    projection = {field: 1 for field in fields}
    order = await Order.get(id, projection=projection)
    if order:
        return order
    return None
