import requests
import json
from datetime import datetime


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/web/2/user/get-status/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.__user_get_status(user_id)
        last_action_time = json_data["lastActionTime"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


if __name__ == "__main__":
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    print(some_resource_client.get_user_last_action_time("318825e6c281ed3ce89acabf0587d9ba"))
# print(some_resource_client.__user_get_status(1716540895))
# Должен быть ответ {"lastActionTime":1716966629,"timeDiff":1565}
# https://www.avito.ru/web/2/user/get-status/318825e6c281ed3ce89acabf0587d9ba
