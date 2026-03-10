numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# индекс пропущенного элемента
missing_index = numbers.index(None)

# сумма всех чисел из списка
total_sum = sum(num for num in numbers if num is not None)

# количество элементов в списке
count = len(numbers)

# среднее арифметическое
average = round(total_sum / count, 2)

# замена пропуска на среднее арифметическое
numbers[missing_index] = average

print("Измененный список:", numbers)