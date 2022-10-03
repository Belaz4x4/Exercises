"""
Модуль создает превью сообщения, предварительно удаляя из него приветствие.
"""


def extract_preview(message, length):
    first_sentence = separate_first_sentence(message)
    greeting = greeting_check(first_sentence, 'привет', 'добрый день', 'здравствуйте', 'хай')

    if greeting:
        message = message.replace(first_sentence, '')

    return message[:length] + '...'


def separate_first_sentence(message):
    exclamation_point_index = point_index = ellipsis_index = 1000
    if '! ' in message:
        exclamation_point_index = message.find('! ')
    if '. ' in message:
        point_index = message.find('. ')
    return message[:min(exclamation_point_index, point_index) + 2]


def greeting_check(message, *checking_words):
    for word in checking_words:
        if word in message.lower():
            return True



# Тесты:
message1 = ('Добрый день, Иван! '
            'Рассмотрел ваше предложение, есть несколько вопросов. '
            'Позвоните завтра после обеда, пожалуйста')
message2 = ('Вань, привет... Мой босс рассмотрел предложение, '
            'которое ты отправлял. Набери меня завтра после обеда.')
message3 = ('Рассмотрел ваше предложение, есть несколько вопросов. '
            'Позвоните завтра после обеда, пожалуйста.')
message4 = ('Здравствуйте! '
            'Вы оформляли заказ №3871570 в нашем интернет-магазине.'
            'Он упакован и готов к доставке. На какой адрес отправить?')
message5 = 'Приветствуем вас!'

print(extract_preview(message5, 40))

assert extract_preview(message1, 40) == 'Рассмотрел ваше предложение, есть нескол...'
assert extract_preview(message2, 40) == 'Мой босс рассмотрел предложение, которое...'
assert extract_preview(message3, 40) == 'Рассмотрел ваше предложение, есть нескол...'
assert extract_preview(message4, 40) == 'Вы оформляли заказ №3871570 в нашем инте...'
assert extract_preview(message5, 40) == '...'