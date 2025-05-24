import requests
from Diplom_2.api_endpoints import USER_ENDPOINT
# Пришлось прописывать именно через 'Diplom_2.', потому что он не принимал абсолютный путь почему-то
class UserProfileApi:

# Метод обновляет пользователя с авторизацией. new_data - json словарь, token - accessToken
    def update_user_with_auth(self, token, new_data):
        headers = {
            'Authorization': token
        }
        response = requests.patch(USER_ENDPOINT, headers=headers, json=new_data)
        return response

# Метод пытается обновить пользователя без передачи accessToken - token
    def update_user_without_auth(self, new_data):
        response = requests.patch(USER_ENDPOINT, json=new_data)
        return response