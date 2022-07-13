'''
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in
the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top
card is still on top.

For example, faro shuffling the list

['ace', 'two', 'three', 'four', 'five', 'six']
gives

['ace', 'four', 'two', 'five', 'three', 'six' ]
If 8 perfect faro shuffles are performed on a deck of 52 playing cards, the deck is restored to its original order.

Write a function that takes an integer n and returns an integer representing the number of faro shuffles it takes to
restore a deck of n cards to its original order.

Assume n is an even number between 2 and 2000.
'''

def faro_cycles(deck_size):
    '''
    Функция принимает размер колоды и генерирует последовательность. Далее применяет цикл Фаро пока новая
    последовательность не совпадет с изначальной. Возвращает количество примененных последовательностей.
    '''
    deck = list(range(deck_size))
    deck_2 = list(range(deck_size))
    a = int(deck_size / 2) - 1
    ans = 1
    n = 1
    for i in range(1, deck_size, 2):
        deck.insert(i, deck[a + n])
        n += 1
        del deck[a + n]
    while deck != deck_2:
        n = 1
        for i in range(1, deck_size, 2):
            deck.insert(i, deck[a + n])
            n += 1
            del deck[a + n]
        ans += 1

    return ans

# tests:
# print(faro_cycles(2))
# print(faro_cycles(4))
# print(faro_cycles(6))
# print(faro_cycles(52))
# print(faro_cycles(8))
# print(faro_cycles(2000))