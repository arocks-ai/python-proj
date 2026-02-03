from fastapi import FastAPI
from socialhub.api.routers.posts import router as posts_router
from contextlib import asynccontextmanager
from socialhub.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(posts_router)
