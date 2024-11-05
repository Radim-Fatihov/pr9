import random

def generate_ticket():
 ticket = []
 for _ in range(5):
  row = sorted(random.sample(range(1, 26), 5))
  ticket.append(row)
 return ticket

def get_user_choice(ticket):
 user_numbers = []
 for i in range(5):
  while True:
   try:
    choice = int(input(f"Выберите число из строки {i + 1}: {ticket[i]} "))
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
 ticket = generate_ticket()
 print("Лотерейный билет:")
 for i, row in enumerate(ticket):
  print(f"Строка {i + 1}: {row}")

 user_numbers = get_user_choice(ticket)
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
