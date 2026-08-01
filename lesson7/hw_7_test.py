def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """
    count = 1
    def mid_func(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            while count < repeat_count:
                func()
                count += 1
            if repeat_count == 0 :
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return mid_func


@repeat_decorator(2)
def example_function():
    print("Hello World!")

# Перевірка
print(example_function())
#assert example_function() is None


# def additional_logic(func):
#     count = 1
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#         nonlocal count
#         count += 1
#     return wrapper
#
#
# @additional_logic
# def hello():
#     print("Hello World!")
#
# hello()