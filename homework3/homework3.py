numbers = []
while True:
 user_input = input("Введите число (или 'end' для завершения): ")
 if user_input.lower() == 'end':
  break
 else:
  try:
   numbers.append(int(user_input))
  except ValueError:
   print("Некорректный ввод. Введите число.")

print("Введенные числа:", numbers)
print("Нечетные числа:", [num for num in numbers if num % 2 != 0])
