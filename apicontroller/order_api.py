import requests
from Diplom_2.api_endpoints import ORDER_ENDPOINT

class OrderApi:

#Метод описывает оба случая: когда токен передается и когда нет
    def get_orders(self, token=None):
        #Если передается token, то мы в заголовки добавляем Authorization
        headers = {'Authorization': token} if token else {}
        return requests.get(ORDER_ENDPOINT, headers=headers)
