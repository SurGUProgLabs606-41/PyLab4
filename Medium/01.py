import functools

def optional_param_decorator(active=True):
    def decorator(func):
        @functools.wraps(func)  # Сохраняем имя и документацию оригинальной функции
        def wrapper(*args, **kwargs):
            if active:
                print(f"Декоратор активен. Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
            result = func(*args, **kwargs)
            if active:
                print(f"Функция {func.__name__} завершила выполнение. Результат: {result}")
            return result
        return wrapper
    return decorator

# Пример использования с опциональным параметром
@optional_param_decorator(active=True)  # Декоратор активен
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Рекурсивный вызов

# Пример использования без опционального параметра (по умолчанию active=True)
@optional_param_decorator()  # Декоратор активен
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный вызов

# Пример использования с отключенным декоратором
@optional_param_decorator(active=False)  # Декоратор неактивен
def sum_numbers(a, b):
    return a + b

# Тестирование
print("Факториал (декоратор активен):")
print(factorial(5))  # 120

print("\nЧисло Фибоначчи (декоратор активен):")
print(fibonacci(5))  # 5

print("\nСумма чисел (декоратор неактивен):")
print(sum_numbers(10, 20))  # 30