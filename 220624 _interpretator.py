'''
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a \texttt{ operator } ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число -− результат вычисления.
'''
def interpretator(e:str):
    '''
    Функция интерпретирует выражение в центре строки в символ математической операции и возвращает результат в виде
    целого числа
    '''
    exp = e.split()
    a, b = int(exp[0]), int(exp[2])
    if exp[1] == "plus":
        return a + b
    if exp[1] == "minus":
        return a - b
    if exp[1] == "multiply":
        return a * b
    if exp[1] == "divide":
        if int(exp[2]) != 0:
            return a // b

e = input()
print(interpretator(e))

# test
# print(interpretator("45 plus 8"))
# print(interpretator("12 minus 42"))
# print(interpretator("451 multiply 2"))
# print(interpretator("13 divide 3"))
# print(interpretator("0 divide 3"))
# print(interpretator("13 divide 0"))
# print(interpretator("451 multiply 0"))