numbers = [3, 7, 10, 9, 1, 5, 8]

for i in range(1, len(numbers)):
 if numbers[i] > numbers[i - 1]:
  print(numbers[i])
