"""5.
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]"""

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, uniqueness=False):
    """
    Функция возращает случайные шутки из трех списков слов.
    :param n: количество случайных шуток
    :param uniqueness: флаг ставить если необходимы уникальные шутки
    :return: список случайных шуток
    """
    listOfJoke = []
    while int(len(nouns)) and n:
        numRandom = randrange(len(nouns))
        if uniqueness:
            listOfJoke.append(f'{nouns.pop(numRandom)} {adverbs.pop(numRandom)} {adjectives.pop(numRandom)}')
        else:
            listOfJoke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return listOfJoke


print(get_jokes(12, uniqueness=True))
