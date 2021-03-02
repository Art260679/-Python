"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split('<CharCode>')


def currency_rates():
    """
    :return: Функция возвращает курс валюты по отношению к рублю
    """
    myDict = {}
    charCode = []
    value = []

    for i in content:
        if i[:3].isalpha():
            charCode.append(i[:3])
        d = str(i.split('<Value>')).split('</Value>')[0].replace("', '", "   ")[-10:].replace(' ', '').replace(',', '.')
        value.append(d)
    del value[0]

    for k, v in zip(charCode, value):
        myDict.setdefault(k, float(v))

    print(f'Список кодов: {myDict.keys()}')

    while True:
        q = input('Введите код валюты: ')
        if q.upper() in myDict.keys():
            return print(f'{q.upper()} = {myDict.get(q.upper())}')
        else:
            print(f'{myDict.get(q.upper())}. Вы ввели не корректное значение.')


currency_rates()
