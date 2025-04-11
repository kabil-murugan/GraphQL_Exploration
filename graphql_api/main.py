"""Main entry point for the FastAPI application."""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from graphql_api.db.init_db import init_db
from graphql_api.graphql.schema import schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Add startup and shutdown events to the FastAPI app."""
    await init_db()
    yield


graphql_app = GraphQLRouter(schema=schema)


app = FastAPI(lifespan=lifespan)
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
