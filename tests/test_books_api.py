from fastapi.testclient import TestClient
from fastapi import status

VALID_CREDENTIALS = ("admin", "123456")
INVALID_CREDENTIALS = ("wrong", "user")

def test_create_book_with_auth_should_succeed(client: TestClient):
    response = client.post(
        "/api/v1/books/",
        json={"title": "A Vida de Larissa Branch", "author": "Rute Luzr", "year": 2015, "isbn": "524522"},
        auth=VALID_CREDENTIALS
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "A Vida de Larissa Branch"
    assert "id" in data

def test_create_book_without_auth_should_fail(client: TestClient):
    response = client.post(
        "/api/v1/books/",
        json={"title": "Kobe", "author": "Bryant", "year": 20225, "isbn": "5678912034"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_list_books_should_succeed(client: TestClient):
    response = client.get("/api/v1/books/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)

def test_book_lifecycle(client: TestClient):
    create_response = client.post(
        "/api/v1/books/",
        json={"title": "Consistência é a chave", "author": "Augusto Loier", "year": 2004, "isbn": "191714236"},
        auth=VALID_CREDENTIALS
    )
    assert create_response.status_code == status.HTTP_201_CREATED
    book_id = create_response.json()["id"]

    get_response = client.get(f"/api/v1/books/{book_id}")
    assert get_response.status_code == status.HTTP_200_OK
    assert get_response.json()["title"] == "Consistência é a chave"

    update_response = client.put(
        f"/api/v1/books/{book_id}",
        json={"title": "Martin Luther", "author": "O verdadeiro The King", "year": 2006, "isbn": "31489376421"}
    )
    assert update_response.status_code == status.HTTP_200_OK
    assert update_response.json()["title"] == "Martin Luther"

    delete_response = client.delete(f"/api/v1/books/{book_id}", auth=VALID_CREDENTIALS)
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    get_after_delete_response = client.get(f"/api/v1/books/{book_id}")
    assert get_after_delete_response.status_code == status.HTTP_404_NOT_FOUND
