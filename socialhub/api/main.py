from fastapi import FastAPI
from socialhub.api.routers.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router)
# app.include_router(posts_router, prefix="/posts", tags=["posts"]) # Optional: add prefix and tags for better organization in docs