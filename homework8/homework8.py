import random

ticket = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
]

def get_user_choice():
  """Запрашивает у пользователя выбор пяти чисел."""
  user_numbers = []
  for i in range(5):
    while True:
      try:
        choice = int(input(f"Выберите число из строки {i + 1}: "))
        if choice in ticket[i]:
          user_numbers.append(choice)
          break
        else:
          print(f"Некорректный ввод. Выберите число из строки {i + 1}: {ticket[i]}")
      except ValueError:
        print("Некорректный ввод. Введите число.")
  return user_numbers

def play_lottery():
  """Запускает игру."""
  user_numbers = get_user_choice()
  random_numbers = [random.choice(row) for row in ticket]
  matches = sum(1 for num in user_numbers if num in random_numbers)
  print("Ваши числа:", user_numbers)
  print("Случайные числа:", random_numbers)
  print(f"Количество совпадений: {matches}")
  if matches == 5:
    print("Поздравляем! Вы выиграли!")
  else:
    print("Повезет в следующий раз!")

if __name__ == "__main__":
  play_lottery()
