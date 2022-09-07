"""
Эта программа генерирует случайные математические примеры на сложение, вычетание и умножение
и проверяет ответы пользователя в бесконечном цикле.

stop, '' - выход из программы
"""
from random import randint

print('Эта программа генерирует случайные математические примеры на сложение, вычетание и умножение и проверяет ваши ответы.')

while True:
  max_number = input('Введите максимально возможное число в примере: ')
  if max_number == 'stop' or max_number == '':
    quit()
  try:
    max_number = int(max_number)
    break
  except ValueError:
    print('Неверное значение! Введите число цифрами или остановите программу введя пустое значение или "stop"')
    continue

print()

while True:
  a = randint(-max_number, max_number)
  b = randint(-max_number, max_number)
  operator = randint(1, 3)
  if operator == 1:
    answer = a + b
    math_question = f'{a} + {b} ='
  elif operator == 2:
    answer = a - b
    math_question = f'{a} - {b} ='
  else:
    answer = a * b
    math_question = f'{a} * {b} ='

  while True:
    users_answer = input(f'{math_question} ?\n')
    if users_answer == 'stop' or users_answer == '':
      quit()
    try:
      users_answer = int(users_answer)
      break
    except ValueError:
      print('Неверное значение! Введите число цифрами или остановите программу введя пустое значение или "stop"')
      continue

  if users_answer == answer:
    print('Верно!')
  else:
    print(f'Неверно! {math_question} {answer}')

  print()