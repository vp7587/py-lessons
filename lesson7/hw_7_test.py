def square_numbers(numbers):
    """
    Замінює кожне число у списку його квадратом.

    :param numbers: Список чисел.
    :return: Новий список з квадратами чисел.
    """
    numbers = list(numbers)
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

# Перевірка
assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
assert square_numbers([]) == []

a = square_numbers
