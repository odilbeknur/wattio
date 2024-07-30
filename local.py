import datetime
import requests
import time
from pymodbus.client.serial import ModbusSerialClient as ModbusClient
from modbus_app import Inverter

ip = '10.40.9.118' + ':8080'
data = {"username": "controller.tpp",
        "password": "1"}

id_controller = '66a721dba453514806c2ddee'
controllers_url = f"http://{ip}/controller/{id_controller}"


def auth(address, log_pass):
    # Получение токена
    url_auth = f"http://{address}/user/signin"
    response = requests.post(url_auth, data=log_pass)
    token = response.json().get("access_token")
    return token


def create_controllers(create_data):
    res = ModbusClient(**create_data)
    return res


def get_url(url, token):
    # Использование токена для доступа к защищенным данным
    secure_url = url
    headers = {
        "Authorization": f"Bearer {token}"
    }
    secure_response = requests.get(secure_url, headers=headers)
    return secure_response.json()


jwt_token = auth(address=ip, log_pass=data)

connect_data = get_url(url=controllers_url, token=jwt_token)['connect']
connect = create_controllers(connect_data)

print(connect)

print(connect_data)

# def create_inverters(connect, create_data):
#     inverters = list()
#     for i in create_data:
#         inverters.append(Inverter(connect=connect, **i))
#     return inverters
#
#
# print(create_inverters(connect, ))
# url = f"http://{ip}/inverter"
#
# response = requests.get(url)
# date = response.json()
# inv_list = list()
#
#
#
# for inv in date:
#     serial_number = str(read_serial_number(connect, inv['slave']))
#     print(serial_number)
#
#     date_reg = {k: ModBusDataRead(**v) for k, v in inv['registers'].items()}
#     inv_list.append(Device(connect=connect, serial_number=serial_number, slave=inv['slave'], read_dict=date_reg))
#
#
# def send_all_register_data(server_ip, data):
#     secure_response = requests.post(server_ip, json=data)
#     return secure_response, secure_response.json()

#
# url_date_send = f"http://{ip}/date"
#
#
# # Задаем интервал в минутах, через который нужно отправлять данные
# interval_minutes = 5
#
# while True:
# try:
#     # Получаем текущее время
#     current_time = datetime.datetime.now()
#
#     # Проверяем условие для отправки данных (каждые interval_minutes минут, в начале минуты)
#     if current_time.minute % interval_minutes == 0 and current_time.second == 0:
#         # Отправляем данные
#         for i in inv_list:
#             print(i.send_all_register_data(url_date_send))
#
#         # Пауза до конца текущей минуты, чтобы избежать повторной отправки в эту же минуту
#         time.sleep(60 - current_time.second)
#     else:
#         # Если не время отправки, ждем некоторое время (например, 1 секунду)
#         time.sleep(1)
# except Exception as e:
#     print(e)
