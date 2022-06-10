'''
Напишите программу, которая выводит nn первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).

Формат ввода:
Строка, содержащая одно целое число nn, n \gt 0n>0.

Формат вывода:
Строка, содержащая требуемую последовательность чисел, разделённых пробелом.

Sample Input:

7
Sample Output:

1 2 2 3 3 3 4
'''
#Создать список, представляющий собой заданную последовательность, после чего вывести первые n элементов.
# n = int(input())
# ans =[]
# for i in range(1, n+1):
#     if len(ans) <= n:
#         for j in range(1, i+1):
#             ans.append(i)
#     else:
#         break
#
# print(*ans[:n])

#Печатать новые элементы сразу, не используя хранение элементов списка.
# n = int(input())
#
# def sequence(n):
#     for i in range(n):
#         for _ in range(i):
#             yield i
#
# ans = sequence(n)
# for _ in range(n): print(next(ans), end=" ")

#Напишите функцию-генератор, которая создаёт бесконечную последовательность, и выведите только первые n членов этой последовательности.
# n = int(input())
#
# def sequence():
#     cnt = 0
#     while True:
#         cnt += 1
#         for _ in range(cnt):
#             yield cnt
#
# ans = sequence()
# for _ in range(n): print(next(ans), end=" ")

#Напишите функцию, которая вычисляет i-й элемент последовательности по его номеру, не вычисляя предыдущие элементы последовательности.
n = int(input())

def sequence(n):
    cnt = 0
    digit = 0
    for i in range(n):
        digit += i
        if digit < n:
            cnt += 1
        else:
            return cnt

print(sequence(n))