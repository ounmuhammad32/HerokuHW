"""This test the homepage"""
def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" aria-current="page" href="/about">About</a>' in response.data
def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data
def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data
def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 404
