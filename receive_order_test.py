import sender_send_request
import data
import pytest

def test_order_info ():
    # new_order = sender_send_request.post_new_orders()
    # track_id = sender_send_request.get_track()
    status_code = sender_send_request.get_receive_orders().status_code
    exp = 200
    assert status_code == exp



# Ефимкина Анна, 9-ая когорта — Финальный проект. Инженер по тестированию плюс