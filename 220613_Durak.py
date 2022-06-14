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