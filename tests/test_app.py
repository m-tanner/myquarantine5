import pytest
from flask import current_app

from src.app import create_app, db
from src.app.models import Role


@pytest.fixture(autouse=True)
def app():
    app = create_app("testing")
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture(autouse=True)
def resource(app):
    db.create_all()
    Role.insert_roles()
    yield resource
    db.session.remove()
    db.drop_all()


def test_app_exists(resource):
    assert current_app is not None


def test_app_is_testing(resource):
    assert current_app.config["TESTING"]
