import databases
import sqlalchemy
from socialhub.config import config 



metadata = sqlalchemy.MetaData()

post_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("message", sqlalchemy.String)
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("message", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False)
)

# SQLLIte - Allows requests from multiple threads (needed in mulithreaded FastAPI app)

# config.DATABASE_URL="sqlite:///./dev-data.db"
print("=== config.DATABASE_URL = ", {config.DATABASE_URL})
print("=== config.DB_FORCE_ROLLBACK = ", {config.DB_FORCE_ROLLBACK})

engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLLBACK
)