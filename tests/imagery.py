from flask.testing import FlaskClient

from tests import client


def test_get_imagery_success(client: FlaskClient):
    """Fetch a single PNG XYZ map tile and confirm success of the response.

    Args:
        client (FlaskClient): Pytest Flask client server fixture

    Returns:
        None
    """

    response = client.get("/imagery/13/1970/2960.png")

    assert response.status_code == 200
    assert response.content_type == "image/png"
    assert isinstance(response.data, bytes)
    assert response.is_json == False


def test_get_imagery_failure(client: FlaskClient):
    """Fetch a single PNG XYZ map tile at an input location that does not exist, and confirm graceful failure of the
    response.

    Args:
        client (FlaskClient): Pytest Flask client server fixture

    Returns:
        None
    """

    response = client.get("/imagery/13/1970/2960abcde.png")

    assert response.status_code == 404
    assert response.content_type == "text/html; charset=utf-8"
    assert isinstance(response.data, bytes)
    assert response.is_json == False


def test_get_imagery_tiles_meta(client: FlaskClient):
    """Fetch metadata about available PNG XYZ map tiles and confirm success of the response.

    Args:
        client (FlaskClient): Pytest Flask client server fixture

    Returns:
        None
    """

    response = client.get("/imagery-tiles")

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert isinstance(response.data, bytes)
    assert response.is_json == True
