# Декоратор для логирования
def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вызвана с аргументами {args}. Результат: {result}")
        return result
    return wrapper

def make_averager():
    numbers = []

    @log_decorator
    def averager(new_number):
        numbers.append(new_number)
        return sum(numbers) / len(numbers)

    return averager

# Пример использования:
avg = make_averager()
print(avg(10))  # 10.0
print(avg(20))  # 15.0
print(avg(30))  # 20.0