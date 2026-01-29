from fastapi import APIRouter, HTTPException
from datetime import datetime

from socialhub.api.models.post import UserPost, UserPostIn, Comment, CommentIn, UserPostWithComments

router = APIRouter()

# In-memory storage for posts
posts_db: list[UserPost] = []       # UserPost Database
comments_db: list[Comment]  = []    # Comments Database (no post info saved)
posts_with_comments: dict[int, list[int]]  # Mapping of post_id to its list of comment_ids


# Base URL
@router.get("/", response_model=dict, tags=["General"], summary="Check API status")
async def root():
    return {"Status": "App is running"}


""""
post realted endpoints

"""

# Create a new post
@router.post("/posts", response_model=UserPost, status_code=201, tags=["Posts"], summary="Create a new post")
async def create_post(post_in: UserPostIn):
    input_data = post_in.dict()
    post_id = len(posts_db)
    post = UserPost(id=post_id, created_at=datetime.utcnow(), **input_data)
    posts_db.append(post)
    return post



# retrieve all posts
@router.get("/posts", response_model=list[UserPost], tags=["Posts"], summary="Retrieve all posts")
async def get_posts():
    return posts_db


# retrieve a single post by ID
@router.get("/posts/{post_id}", response_model=UserPost, tags=["Posts"], summary="Get Post by Id")
async def get_post(post_id: int):
    for post in posts_db:
        if post.id == post_id:
            return post        
    else:    
        raise HTTPException(status_code=404, detail="Post not found")


# retrieve a single post and comments by ID
@router.get("/posts/{post_id}/comments", response_model=UserPostWithComments, \
            tags=["Posts"], summary="Get Post by Id")
async def get_post_with_comments(post_id: int):
    # First find post by ID
    post_to_use :UserPost
    for post in posts_db:
        if post.id == post_id:
            post_to_use =  post
            break
    else:    
        raise HTTPException(status_code=404, detail="Post not found")
    


    # Now find comments related to this post
    related_comments :list[Comment] = []
    for comment in comments_db:
        if comment.post_id == post_id:
            related_comments.append(comment)
    post_with_comments = UserPostWithComments(post=post_to_use, comments=related_comments)
    return post_with_comments

""""
comments realted endpoints
"""


# Create a comment for a specific post
@router.post("/comments", response_model=Comment, status_code=201,\
                tags=["Comments"], summary="Create a comment for a specific post")
async def create_post(comment_in: CommentIn):
        
    # Check if post exists
    post_to_use :UserPost
    for post in posts_db:
        if post.id == comment_in.post_id:
            post_to_use = post
            break
    else:
        raise HTTPException(status_code=404, detail="Post not found")

    # Save comments to Database
    input_data = comment_in.dict()        
    comment_id = len(comments_db)        
    new_comment = Comment(id=comment_id, **input_data)
    comments_db.append(new_comment)

    return new_comment



# retrieve a single post by ID
@router.get("/comments/{comment_id}", response_model=Comment, 
            tags=["Comments"], summary="Get Comment by Id")
async def get_post(comment_id: int):
    for comment in comments_db:
        if comment.id == comment_id:
            return comment
        
    raise HTTPException(status_code=404, detail="Comment not found")