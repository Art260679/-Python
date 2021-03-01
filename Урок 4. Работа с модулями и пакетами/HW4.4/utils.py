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
