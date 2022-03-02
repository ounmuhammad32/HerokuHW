"""This test the homepage"""
def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" aria-current="page" href="/about">about</a>' in response.data
def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Oun Muhammad" in response.data
def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"about" in response.data
def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 404
