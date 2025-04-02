import pytest 
import requests
import json


order_id = 2
order_petId = 25079155
order_quantity = 1
order_shipDate = "2025-04-02T11:28:21.083+0000"
order_status = "placed"
order_complete = True
url = "https://petstore.swagger.io/v2/store/order"
headers = {"Content-Type": "application/json"}


def test_post_store_order():
    order = open("./fixtures/json/order1.json") 
    data = json.loads(order.read())
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == order_id
    assert response_body ["petId"] == order_petId
    assert response_body ["quantity"] == order_quantity
    assert response_body ["shipDate"] == order_shipDate
    assert response_body ["status"] == order_status
    assert response_body ["complete"] == order_complete

def test_get_store_order():
    order = open("./fixtures/json/order1.json") 
    data = json.loads(order.read())
    response = requests.get(
        url = f"{url}/{order_id}",
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response_body ["id"] == order_id
    assert response_body ["petId"] == order_petId
    assert response_body ["quantity"] == order_quantity
    assert response_body ["shipDate"] == order_shipDate
    assert response_body ["status"] == order_status
    assert response_body ["complete"] == order_complete

def test_delete_store_order():
    order = open("./fixtures/json/order1.json") 
    data = json.loads(order.read())
    response = requests.delete(
        url = f"{url}/{order_id}",
        headers = headers,
        data = json.dumps(data),
        timeout=5
    )
    response_body = response.json()
    assert response_body ["code"] == 200
    assert response_body ["type"] == "unknown"
    assert response_body ["message"] == str(order_id)