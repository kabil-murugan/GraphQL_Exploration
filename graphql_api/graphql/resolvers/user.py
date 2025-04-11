from typing import List, Optional

import strawberry

from graphql_api.models.user import User


async def get_users(fields: List[str]) -> List[User]:
    """Fetch all users."""
    projection = {field: 1 for field in fields}
    return await User.find_all(projection=projection).to_list()


async def get_user(id: strawberry.ID, fields: List[str]) -> Optional[User]:
    """Fetch a user by ID."""
    projection = {field: 1 for field in fields}
    user = await User.get(id, projection=projection)
    if user:
        return user
    return None
