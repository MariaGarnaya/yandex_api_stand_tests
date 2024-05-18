# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration
import requests
import data



def get_docs():

    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()

print(response.status_code)

# Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

# Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
response = get_logs()


print(response.status_code)

print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()

print(response.status_code)

def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body);

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)
print(response.json())


# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,  # Тело запроса содержит ID продуктов в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py

# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.product_ids)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
print(response.status_code)
print(response.json())



