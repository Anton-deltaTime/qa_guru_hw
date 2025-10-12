from datetime import datetime, timezone
from typing import Callable

import allure
import pytest

from resources.schemas import ReqresPostMethodUsers, ReqresGetMethodUsers, ReqresGetMethodUsersByID, ReqresPutMethodUsersByID


@pytest.mark.reqres_method
@allure.feature("Проверка GET запроса метода api/users")
@pytest.mark.parametrize('send_request', [('get', 'api/users')], indirect=True, ids=["get_users"])
def test_get_all_users(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        params = {"page": 1, "per_page": 25}
        response = send_request(params=params)
    assert response.status_code == 200

    response_json = response.json()
    response_json.pop('_meta')
    with allure.step('Проверка схемы ответа'):
        ReqresGetMethodUsers(**response_json)

    assert response_json["page"] == params["page"], "Параметр page не соответствует переданному значению"
    assert response_json["per_page"] == params["per_page"], "Параметр per_page не соответствует переданному значению"
    assert len(response_json["data"]) == response_json["total"], "Количество пользователей в data не соответствует значению total"

    for user in response_json["data"]:
        assert user['email'] == f"{user['first_name'].lower()}.{user['last_name'].lower()}@reqres.in", "email состоит не из параметров first_name и last_name, и домена @reqres.in"


@pytest.mark.reqres_method
@allure.feature("Проверка POST запроса метода api/users с передачей email")
@pytest.mark.parametrize('send_request', [('post', 'api/users')], indirect=True, ids=["post_user"])
def test_post_email(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        json_data = {"email": "test.test@test.tt"}
        response = send_request(json=json_data)
    assert response.status_code == 201

    response_json = response.json()
    with allure.step('Проверка схемы ответа'):
        ReqresPostMethodUsers(**response_json)

    assert response_json["id"], "В ответе отсутствует id пользователя"
    assert response_json["email"] == json_data["email"], "Переданные email не совпадает с ответом"
    r_date = datetime.fromisoformat(response_json["createdAt"])
    now = datetime.now(timezone.utc)
    assert (r_date.year, r_date.month, r_date.day, r_date.hour, r_date.minute) == (now.year, now.month, now.day, now.hour, now.minute), "В ответе не текущая дата"


@pytest.mark.reqres_method
@allure.feature("Проверка GET запроса метода api/users/{user_id}")
@pytest.mark.parametrize('send_request', [('get', 'api/users/1')], indirect=True, ids=["get_user_id_1"])
def test_get_user_by_id(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        response = send_request()
    assert response.status_code == 200

    response_json = response.json()
    response_json.pop('_meta')
    with allure.step('Проверка схемы ответа'):
        ReqresGetMethodUsersByID(**response_json)

    assert isinstance(response_json["data"], dict), "Был передан список юзеров вместо одного пользователя"
    user = response_json["data"]
    assert user['id'] == 1, "id юзера отличается от запрошенного номера 1"
    assert user['email'] == f"{user['first_name'].lower()}.{user['last_name'].lower()}@reqres.in", "email состоит не из параметров first_name и last_name, и домена @reqres.in"


@pytest.mark.reqres_method
@allure.feature("Проверка PUT запроса метода api/users/{user_id}")
@pytest.mark.parametrize('send_request', [('put', 'api/users/1')], indirect=True, ids=["put_user_id_1"])
def test_put_user_by_id(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        json_data = {
            "email": "test.test@reqres.in",
            "first_name": "test_Arkan",
            "last_name": "test_Roklan",
            "avatar": "https://reqres.in/img/faces/test.png"
        }
        response = send_request(json=json_data)
    assert response.status_code == 200

    response_json = response.json()
    with allure.step('Проверка схемы ответа'):
        ReqresPutMethodUsersByID(**response_json)

    assert response_json['email'] == json_data['email'], "В ответе значение отличается от переданного"
    assert response_json['first_name'] == json_data['first_name'], "В ответе значение отличается от переданного"
    assert response_json['last_name'] == json_data['last_name'], "В ответе значение отличается от переданного"
    assert response_json['avatar'] == json_data['avatar'], "В ответе значение отличается от переданного"


@pytest.mark.reqres_method
@pytest.mark.xfail(reason="TASK-5 в PUT методе /api/users/{user_id} нельзя передавать id юзера")
@allure.feature("Проверка PUT запроса метода api/users/{user_id} с передачей id")
@pytest.mark.parametrize('send_request', [('put', 'api/users/1')], indirect=True, ids=["put_user_id_1_fail"])
def test_put_user_by_id_fail(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        json_data = {
            "id": 13
        }
        response = send_request(json=json_data)
    assert response.status_code == 400


@pytest.mark.reqres_method
@allure.feature("Проверка DELETE запроса метода api/users/{user_id}")
@pytest.mark.parametrize('send_request', [('delete', 'api/users/1')], indirect=True, ids=["delete_user_id_1"])
def test_delete_user_by_id(send_request: Callable):
    with allure.step('Выполнение запроса в API'):
        response = send_request()
    assert response.status_code == 204
