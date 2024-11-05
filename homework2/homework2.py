def squares_between(a, b):

  if b <= a:
    raise ValueError("Число b должно быть больше числа a.")

  squares = []
  for i in range(int(a) + 1, int(b)):
    squares.append(i ** 2)

  if int(a) != a or int(b) != b:
    for i in range(int(a) + 1, int(b)):
      for j in range(1, 10):
        num = i + j / 10
        if a < num < b:
          squares.append(num ** 2)

  return squares

if __name__ == "__main__":
  try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))

    squares_list = squares_between(a, b)
    print(f"Список квадратов чисел между {a} и {b}: {squares_list}")

  except ValueError as e:
    print(f"Ошибка: {e}")








