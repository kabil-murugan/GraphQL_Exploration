from typing import List

import strawberry

from graphql_api.graphql.resolvers.order import get_orders
from graphql_api.graphql.resolvers.product import get_products
from graphql_api.graphql.resolvers.user import get_users
from graphql_api.graphql.types.order import Order
from graphql_api.graphql.types.product import Product
from graphql_api.graphql.types.user import User


@strawberry.type
class Query:
    @strawberry.field(graphql_type=List[User])
    async def users(self, info: strawberry.Info):
        fields = [
            field.name
            for field in info.selected_fields
            if type(field) is strawberry.types.nodes.SelectedField
        ]
        return await get_users(fields)

    @strawberry.field(graphql_type=List[Order])
    async def orders(self, info: strawberry.Info):
        fields = [
            field.name
            for field in info.selected_fields
            if type(field) is strawberry.types.nodes.SelectedField
        ]
        return await get_orders(fields)

    @strawberry.field(graphql_type=List[Product])
    async def products(self, info: strawberry.Info):
        fields = [
            field.name
            for field in info.selected_fields
            if type(field) is strawberry.types.nodes.SelectedField
        ]
        return await get_products(fields)

    # @strawberry.field
    # async def user(self, id: strawberry.ID) -> User:
    #     pass

    # @strawberry.field
    # async def order(self, id: strawberry.ID) -> Order:
    #     pass

    # @strawberry.field
    # async def product(self, id: strawberry.ID) -> Product:
    #     pass


schema = strawberry.Schema(query=Query)
