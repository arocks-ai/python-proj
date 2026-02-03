import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


ENV = os.getenv("ENV", "dev")   # default = dev

class ConfigSettings(BaseSettings):
    DATABASE_URL: str
    DB_FORCE_ROLLBACK: bool = False

    class Config:
        # env_file = f"env/{ENV}.env"
        env_file = f"socialhub/.env"
        env_file_encoding = "utf-8"


config = ConfigSettings()



"""
OLD Code is below.
"""


# class BaseConfig(BaseSettings):
#     ENV_STATE: Optional[str] = None

#     """Loads the dotenv file. Including this is necessary to get
#     pydantic to load a .env file."""
#     model_config = SettingsConfigDict(env_file=".env", extra="ignore")



# class GlobalConfig(BaseConfig):
#     DATABASE_URL: Optional[str] = None
#     DB_FORCE_ROLLBACK: bool = False
    

# class DevConfig(GlobalConfig):
#     model_config = SettingsConfigDict(env_prefix="DEV_")     # DATABASE_URL will be DEV_DATABASE_URL


# class TestConfig(GlobalConfig):
#     model_config = SettingsConfigDict(env_prefix="TEST_")


# class ProdConfig(GlobalConfig):
#     model_config = SettingsConfigDict(env_prefix="PROD_")


# @lru_cache()
# def get_config(env: str):
#     """Instantiate config based on the environment."""

#     if env == "prod":
#         return ProdConfig()
#     elif env == "test":
#         return TestConfig()
#     else:
#         return DevConfig()  # default is dev
    

# # config = get_config(BaseConfig().ENV_STATE)
# config = get_config("dev")

