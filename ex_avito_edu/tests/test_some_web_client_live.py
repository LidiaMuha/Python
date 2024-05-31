from datetime import datetime
import pytest
from ex_avito_edu.some_web_client_live import SomeResourceClient
import responses


# но нельзя ходить на прод напрямую, не использовать внешние
# сервисы во время тестов
# для этого используют заглушки (мок)


# позитивный тест
@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1716971523,
        "timeDiff": 245
    }
    responses.add(method=responses.GET,
                  url="https://www.avito.ru/web/2/user/get-status/318825e6c281ed3ce89acabf0587d9ba",
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time("318825e6c281ed3ce89acabf0587d9ba")
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])


# негативный тест (со знаком "-")
@responses.activate
def test_some_web_client_with_error():
    valid_json_answer = {
        "errors": [
            "Not found"
        ]
    }
    responses.add(method=responses.GET,
                  url="https://www.avito.ru/web/2/user/get-status/318825e6c281ed3ce89acabf0587d9ba-",
                  json=valid_json_answer, status=404)
    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient("https://www.avito.ru")
        some_resource_client.get_user_last_action_time("318825e6c281ed3ce89acabf0587d9ba-")
