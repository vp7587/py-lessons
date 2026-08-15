# file_name = "text.txt"
#
# new_file_name = str(file_name).replace(".txt", "_new.txt")
#
# print(new_file_name)
#
# newline = "[]''"
# newline = str(newline).replace("[", "")
# print(newline)


# def check_positive(value):
#     if value < 0:
#         raise ValueError('Value must be positive')
#
#
# # Перевірка:
# try:
#     check_positive(5)  # Очікуваний результат: (без виводу, так як немає помилки)
# except Exception as e:
#     print(e) # Достигнут минимум
#
#
# try:
#     check_positive(-3)  # Очікуваний результат: ValueError: Value must be positive
# except Exception as e:
#     print(e) # Достигнут минимум

def safe_divide(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        raise Exception("Error: Division by zero")


# Перевірка:
# try:
#     result = safe_divide(10, 2)
#     print(result)  # Очікуваний результат: 5
# except Exception as e:
#     print(e)
#
# try:
#     result = safe_divide(8, 0)
#     print(result)  # Очікуваний результат: "Error: Division by zero"
# except Exception as e:
#     print(e)
#
# assert safe_divide(15, 3) == 5
#
# assert safe_divide(5, 0) == "Error: Division by zero"

class TemperatureValueError(Exception):
    pass

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        result = (celsius*9/5) + 32
        if result > -273:
            return result
        else:
            raise TemperatureValueError('Invalid temperature value')

# Перевірка:
converter = TemperatureConverter()
result_1 = converter.convert_celsius_to_fahrenheit(25)  # Очікуваний результат: 77.0
print(result_1)

try:
    result_2 = converter.convert_celsius_to_fahrenheit(-300)  # Очікуваний результат: TemperatureValueError: Invalid temperature value
    print(result_2)
except Exception as e:
    print(e)