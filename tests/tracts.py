from flask.testing import FlaskClient

from tests import client

def test_get_tracts_success(client: FlaskClient):
    response = client.get('/tracts/15/7858/11813.json')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.data, bytes)
    assert response.is_json == True

def test_get_tracts_failure(client: FlaskClient):
    response = client.get('/tracts/15/7858/11813abcde.json')

    assert response.status_code == 404
    assert response.content_type == 'text/html; charset=utf-8'
    assert isinstance(response.data, bytes)
    assert response.is_json == False

def test_get_tracts_tiles_meta(client: FlaskClient):
    response = client.get('/tracts-tiles')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.data, bytes)
    assert response.is_json == True