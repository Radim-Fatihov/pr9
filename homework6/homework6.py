def swap_min_max(numbers):

 min_index = numbers.index(min(numbers))
 max_index = numbers.index(max(numbers))

 numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
 return numbers

if __name__ == "__main__":
 numbers = [3, 7, 8, 10, 4, 5, 2]
 print("Исходный список:", numbers)
 numbers = swap_min_max(numbers)
 print("Измененный список:", numbers)
