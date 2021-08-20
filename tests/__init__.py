import pytest

from flask import Flask
from flask.testing import FlaskClient

from flask_app import create_app


@pytest.fixture
def client() -> FlaskClient:
    """Factory for instantiating and initializing vanilla FlaskClient mock testing fixtures.

    Returns:
        FlaskClient: Vanilla Flask mock testing fixture
    """

    app: Flask = create_app()
    client: FlaskClient = app.test_client()
    return client
