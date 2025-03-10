def make_averager():
    numbers = []

    def averager(new_number):
        numbers.append(new_number)
        return sum(numbers) / len(numbers)

    return averager

# Пример использования:
avg = make_averager()
print(avg(10))  # 10.0
print(avg(20))  # 15.0
print(avg(30))  # 20.0

def validate_args(*expected_types, min_value=None, max_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                # Проверяем тип аргумента
                if not isinstance(arg, expected_type):
                    print(f"Предупреждение: Аргумент {i} не является типом {expected_type}")
                    continue  # Пропускаем дальнейшие проверки для этого аргумента

                # Проверяем диапазон значений (только для чисел)
                if min_value is not None and arg < min_value:
                    print(f"Предупреждение: Аргумент {i} меньше {min_value}")
                if max_value is not None and arg > max_value:
                    print(f"Предупреждение: Аргумент {i} больше {max_value}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования:
@validate_args(int, int, min_value=0, max_value=100)
def add(a, b):
    return a + b

print(add(10, 20))  # 30
print(add(-10, 20))  # Предупреждение: Аргумент 0 меньше 0, 10
print(add(110, 20))  # Предупреждение: Аргумент 0 больше 100, 130
#print(add(10, "20"))  # Предупреждение: Аргумент 1 не является типом <class 'int'>, TypeError