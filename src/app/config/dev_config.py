import os

from src.app.config.config import Config


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("MYQ5_DEVTEST_DATABASE_URL")
