def validate_args(*expected_types, min_value=None, max_value=None, verbose=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    if verbose:
                        print(f"Предупреждение: Аргумент {i} не является типом {expected_type}")
                    continue

                if min_value is not None and arg < min_value:
                    if verbose:
                        print(f"Предупреждение: Аргумент {i} меньше {min_value}")
                if max_value is not None and arg > max_value:
                    if verbose:
                        print(f"Предупреждение: Аргумент {i} больше {max_value}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(int, int, min_value=0, max_value=100, verbose=True)  # Включен вывод предупреждений
def add(a, b):
    return a + b

@validate_args(int, min_value=0, verbose=False)  # Отключен вывод предупреждений
def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(add(10, 20))  # 30
print(add(-10, 20))  # Предупреждение: Аргумент 0 меньше 0, 10
print(add(110, 20))  # Предупреждение: Аргумент 0 больше 100, 130
print(factorial(5))  # 120