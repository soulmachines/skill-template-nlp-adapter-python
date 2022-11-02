from pydantic import BaseSettings

class BaseConfig(BaseSettings):
    """
    Base application configuration
    """

    port: int = 3000
    env: str
    debug: bool

    class Config:
        env_file = ".env"
