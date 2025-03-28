import pytest 
import requests
import json


pet_id = 250791
pet_name = "Dante"
pet_category_id = 1
pet_category_name = "Dog"
pet_tags_id = 1
pet_tags_name = "vacinado"
pet_status = "available"
url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}


def test_post_pet():
    pet=open("./fixtures/json/pet1.json")
    data=json.loads(pet.read())
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == pet_id
    assert response_body ["name"] == pet_name
    assert response_body ["category"]["id"] == pet_category_id
    assert response_body ["category"]["name"] == pet_category_name
    assert response_body ["tags"][0]["id"] == pet_tags_id
    assert response_body ["tags"][0]["name"] == pet_tags_name
    assert response_body ["status"] == pet_status


def test_get_pet():
    response = requests.get(
        url = f"{url}/{pet_id}",
        headers = headers
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == pet_id
    assert response_body ["name"] == pet_name
    assert response_body ["category"]["id"] == pet_category_id
    assert response_body ["category"]["name"] == pet_category_name
    assert response_body ["tags"][0]["id"] == pet_tags_id
    assert response_body ["tags"][0]["name"] == pet_tags_name
    assert response_body ["status"] == pet_status

