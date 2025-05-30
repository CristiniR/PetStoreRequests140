import pytest 
import requests
import json


user_id = 1
user_username = "User01"
user_firstName = "User"
user_lastName = "Teste01"
user_email = "teste01@email.com"
user_password = "SenhaUser01"
user_phone = "554799990001"
user_userStatus = 1
url = "https://petstore.swagger.io/v2/user"
headers = {"Content-Type": "application/json"}


def test_post_user():
    user = open("./fixtures/json/user1.json") 
    data = json.loads(user.read())
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response_body ["code"] == 200
    assert response_body ["type"] == "unknown"
    assert response_body ["message"] == str(user_id)


def test_get_user():
    response = requests.get(
        url = f"{url}/{user_username}",
        headers = headers
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == user_id
    assert response_body ["username"] == user_username
    assert response_body ["firstName"] == user_firstName
    assert response_body ["lastName"] == user_lastName
    assert response_body ["email"] == user_email
    assert response_body ["password"] == user_password
    assert response_body ["phone"] == "554799990001"
    assert response_body ["userStatus"] == user_userStatus


def test_put_user():
    user = open("./fixtures/json/user2.json")
    data = json.loads(user.read())
    response = requests.put(
        url = f"{url}/{user_username}",
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == user_id
    assert response_body ["username"] == user_username
    assert response_body ["firstName"] == user_firstName
    assert response_body ["lastName"] == user_lastName
    assert response_body ["email"] == user_email
    assert response_body ["password"] == user_password
    assert response_body ["phone"] == "554799990022"
    assert response_body ["userStatus"] == user_userStatus


def test_delete_user():
    user = open("./fixtures/json/user1.json") 
    data = json.loads(user.read())
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response_body ["code"] == 200
    assert response_body ["type"] == "unknown"
    assert response_body ["message"] == str(user_id)