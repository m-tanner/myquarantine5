import abc
import os


class Config(metaclass=abc.ABCMeta):
    SECRET_KEY = os.getenv("MYQ5_SECRET_KEY", "hard to guess string")
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() in ["true", "on", "1"]
    MAIL_ADDRESS = os.getenv("MYQ5_EMAIL_ADDRESS")
    MAIL_USERNAME = MAIL_ADDRESS.split("@")[0]
    MAIL_PASSWORD = os.getenv("MYQ5_EMAIL_PASSWORD")
    MYQ5_MAIL_SUBJECT_PREFIX = "[MyQuarantine5]"
    MYQ5_MAIL_SENDER = f"MyQuarantine5 Admin <{MAIL_ADDRESS}>"
    MYQ5_ADMIN = os.getenv("MYQ5_ADMIN_EMAIL_ADDRESS")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 20
    FOLLOWERS_PER_PAGE = 50

    @staticmethod
    def init_app(app):
        pass
