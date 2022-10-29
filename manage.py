from functools import lru_cache
import uvicorn
from app.app import create_app
from app.config.base_config import BaseConfig


@lru_cache()
def get_settings():
    return BaseConfig()

config = get_settings()
app = create_app()

if __name__ == "__main__":
    uvicorn.run("manage:app", host="0.0.0.0", port=config.port, reload=config.debug)