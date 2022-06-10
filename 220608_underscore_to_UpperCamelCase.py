"""
Вы решили написать преобразователь кода на Python в код на Java. Так как на Java принят стандарт наименования CamelCase,
то вы решили научиться преобразовывать имена из underscore в этот формат.

Для начала напишите программу, которая переводит имена переменных из стиля написания underscore в стиль UpperCamelCase.

Стиль underscore характеризуется тем, что слова в имени пишутся маленькими буквами и разделяются между собой символом
подчёркивания "_". Стиль UpperCamelCase означает, что каждое слово пишется с большой буквы и разделителей между словами
нет.

Формат ввода:
Одна строка, содержащая имя, записанное в формате underscore.

Формат вывода:
Строка, содержащая пришедшее имя в формате UpperCamelCase.
"""
name = input()


def converter(a: str):
    '''
    Функция конвертирует имена в формате nderscope в UpperCamelCase

    Входящая строка разбивается на список строк по "_", после этого каждое значение списка переписывается с заглавной
    буквы, а список собирается в одну строку.
    '''
    a = a.split("_")
    a = [a[i].capitalize() for i in range(len(a))]
    return "".join(a)


print(converter(name))

# Tests:
# print(converter("my_first_class"))
# print(converter("a"))
# print(converter(""))