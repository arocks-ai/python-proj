# Client send message only
from datetime import datetime
from pydantic import BaseModel, Field


# Represents the message posted by the user.
# client send the message like {"message": "Hello World"}
class UserPostIn(BaseModel):
    message: str

# Holds the Post with metadata.(like ID and created_at timestamp)
# Server calculates these fields like id and created_at
class UserPost(UserPostIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Represents a comment on a post.
class CommentIn(BaseModel):
    message: str
    post_id: int

# Holds the Comment with metadata.(like comment ID)
class Comment(CommentIn):
    id: int


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]



"""
HTTP Endpoints:

General
  GET / — Check API status

Posts
  GET /posts — Retrieve all posts (without comments)
  POST /posts — Create a new post
  GET /posts/{post_id} — Retrieve a post with comments by post ID
  GET /posts/{post_id}/comments — Retrieve comments for a specific post

Comments
  POST /comments — Create a comment for a specific post
  GET /comments/{comment_id} — Retrieve a comment by ID


POST /posts/comments - Invalid Endpoint
GET  /posts/comments - Invalid Endpoint


---



"""




