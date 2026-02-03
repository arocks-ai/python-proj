from typing import AsyncGenerator, Generator
import pytest 
from socialhub.api.main import app

from socialhub.api.routers.posts import posts_table, comments_table




@pytest.fixture()
def client() -> Generator:
    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        yield c

@pytest.fixture()
async def db_cleanup() -> AsyncGenerator:
    posts_table.clear()
    comments_table.clear()