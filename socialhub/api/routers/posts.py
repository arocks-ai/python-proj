from fastapi import APIRouter
from datetime import datetime

from socialhub.api.models.post import UserPost, UserPostIn

router = APIRouter()

# In-memory storage for posts
posts_db: list[UserPost] = []

# Create a new post
@router.post("/posts", response_model=UserPost)
async def create_post(post_in: UserPostIn):
    input_data = post_in.dict()
    post_id = len(posts_db) + 1
    post = UserPost(id=post_id, created_at=datetime.utcnow(), **input_data)
    posts_db.append(post)
    return post


# Base URL
@router.get("/", response_model=dict)
async def root():
    return {"Status": "App is running"}


# retrieve all posts
@router.get("/posts", response_model=list[UserPost])
async def get_posts():
    return posts_db


# retrieve a single post by ID
@router.get("/posts/{post_id}", response_model=UserPost)
async def get_post(post_id: int):
    for post in posts_db:
        if post.id == post_id:
            return post
        
    return {"error": "UserPost not found"}