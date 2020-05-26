import os

from src.app.config.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("MYQ5_DEVTEST_DATABASE_URL")
