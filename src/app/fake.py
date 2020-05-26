from random import randint

from faker import Faker
from sqlalchemy.exc import IntegrityError

from src.app.models import User, Post
from . import db


def users(count=100):
    """
    To be used as a script:
        (venv) % flask shell
        >>> from src.app import fake
        >>> fake.users(100)

    This takes a while to run.
    """
    fake = Faker()
    i = 0
    while i < count:
        user = User(
            email=fake.email(),
            username=fake.user_name(),
            password="password",
            confirmed=True,
            name=fake.name(),
            location=fake.city(),
            about_me=fake.text(),
            housemates=fake.text(),
            significant_others=fake.name(),
            my_five=fake.name(),
            member_since=fake.past_date(),
        )
        db.session.add(user)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            # we somehow got a random duplicate
            db.session.rollback()


def posts(count=100):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(body=fake.text(), timestamp=fake.past_date(), author=u)
        db.session.add(p)
    db.session.commit()
