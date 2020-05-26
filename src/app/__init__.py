from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_seasurf import SeaSurf
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

from src.app.config import config, config_factory

talisman = Talisman()
seasurf = SeaSurf()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_type: str) -> Flask:
    app = Flask(__name__)
    app_config = config_factory.get_config(config_type)
    app.config.from_object(app_config)

    app_config.init_app(app)

    # FIXME
    # talisman.init_app(
    #     app, content_security_policy={"default-src": ["*"]},
    # )
    # seasurf.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    from src.app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from src.app.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
