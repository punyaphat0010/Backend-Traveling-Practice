
def test_user_register(client):
    user_data = {
        "username": "pytestuser",
        "firstname": "Py",
        "lastname": "Test",
        "password": "pytestpass123",
        "phone": "0999999999",
        "email": "pytestuser@example.com"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert data["message"] == "User registered successfully"
