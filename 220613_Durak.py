'''
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For
scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается
козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

Sample Input 1:

AH JH
D
Sample Output 1:

First
Sample Input 2:

AH JS
S
Sample Output 2:

Second
Sample Input 3:

7C 10H
S
Sample Output 3:

Error
'''

def durak(f, s, t):
    '''
    Функция определяет бьет ли одна карта другую в игре Дурак
    '''
    values = ['6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']

    if len(f) == 3:
        f = f.replace('0','')
    if len(s) == 3:
        s = s.replace('0','')

    if s == f:
        return print('Error')
    elif (values.index(f[0]) > values.index(s[0]) and f[1] == s[1]) or (f[1] == t and s[1] != t):
        return print('First')
    elif (values.index(f[0]) < values.index(s[0]) and f[1] == s[1]) or (s[1] == t and f[1] != t):
        return print('Second')
    else:
        return print('Error')

first, second = input().split()
trump = input()

durak(first, second, trump)

# Tests:
# durak('AH', 'JH', 'D')
# durak('AH', 'JS', 'S')
# durak('7C', '10H', 'S')
# durak('7C', '7C', 'C')
# durak('7C', '7C', 'S')
# durak('10C', 'QC', 'C')
# durak('AC', 'QC', 'C')