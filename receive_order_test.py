import sender_send_request
import data
import requests


# Функция для изменения значения в параметре track в теле запроса
def get_orders_body():
    # Копируется словарь с телом запроса из файла data
    current_body = data.orders_body.copy()
    # Изменение значения в поле firstName
    current_body["track"] = "track"
    # Возвращается новый словарь с нужным значением firstName
    return current_body

#Функция проверки
def test_assert_get_orders_by_track():
    # В переменную user_body сохраняется обновленное тело запроса с именем “Аа”
    orders_body = get_orders_body()
    # В переменную user_response сохраняется результат запроса на создание пользователя
    orders_response = sender_send_request.get_receive_orders()

    # Проверяется, что код ответа равен 201
    assert orders_response.status_code == 201

