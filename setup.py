from setuptools import setup, find_packages

install_requirements = [
    "flask",
    "click",
    "waitress",
    "wtforms",
    "flask-wtf",
    "flask-bootstrap",
    "flask-mail",
    "flask-moment",
    "flask-sqlalchemy",
    "flask-migrate",
    "alembic",
    "sqlalchemy",
    "boto3",
    "botocore~=1.14",
    "six~=1.12",
    "google-cloud-storage",
    "pytz",
    "pymysql",
    "psycopg2",
    "flask-login",
    "werkzeug",
    "itsdangerous",
    "faker",
    "email-validator",
    "flask-pagedown",
    "Markdown",
    "bleach",
]

test_requirements = [
    "pytest",
    "pytest-cov",
]

lint_requirements = [
    "black",
    "flake8",
    "pylint",
]

setup(
    name="MyQuarantine5",
    version="0.1",
    packages=find_packages(),
    url="myquarantine5.com",
    license="",
    author="Michael Tanner",
    author_email="tanner.mbt@gmail.com",
    description="pick your favorite five",
    install_requires=install_requirements,
    extras_require={"tests": [test_requirements], "lint": [lint_requirements]},
    python_requires="~=3.7",
    entry_points={"console_scripts": ["myq5_svc=src.app.myq5_waitress:start_serving"]},
)
