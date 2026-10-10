import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Agent Platform",
    )

    APP_VERSION: str = os.getenv(
        "APP_VERSION",
        "1.0.0",
    )

    DEBUG: bool = os.getenv(
        "DEBUG",
        "false",
    ).lower() in ("true", "1", "yes")


settings = Settings()