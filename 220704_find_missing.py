'''
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a
given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one
hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The
rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will
never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on
paper using math, derive the algo that way. Have fun!
'''

def find_missing(sequence):
    '''
    Функция принимает арифметическую прогрессию с одним пропущенным значением и возвращает это значение.
    Поиск происходит через сравнение шага между соседними элементами. Если шаг большой - то к первому элементу
    добавляется интервал и получается пропущенное значение.
    '''
    for i in range(len(sequence)):
        a = sequence[i+1] - sequence[i]
        b = sequence[i+2] - sequence[i+1]
        if a > b:
            return sequence[i] + b
        if b > a:
            return sequence[i+1] + a

#tests:
print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))