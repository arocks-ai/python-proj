from fastapi import FastAPI
from socialhub.api.routers.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router)
