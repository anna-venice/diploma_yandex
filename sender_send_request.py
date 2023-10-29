import configuration
import requests
import data


#Cоздание заказа

def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.orders_body)

#Сохранение номера заказа

def get_track():
    track_number = post_new_orders().json()["track"]
    return track_number
# print(get_track())

#Получение заказа

def get_receive_orders():
    track_id=get_track()
    str_track_id = str(track_id)
    return requests.get (configuration.URL_SERVICE + configuration.RECEIVE_ORDERS_TRACK+ str_track_id)


