import functools

def optional_param_decorator(active=True):
    def decorator(cls):
        # Перебираем все атрибуты класса
        for name, method in vars(cls).items():
            if callable(method):  # Проверяем, что атрибут является методом
                # Декорируем метод
                @functools.wraps(method)
                def wrapper(*args, **kwargs):
                    if active:
                        print(f"Декоратор активен. Вызов метода {name} с аргументами {args} и {kwargs}")
                    result = method(*args, **kwargs)
                    if active:
                        print(f"Метод {name} завершил выполнение. Результат: {result}")
                    return result
                # Заменяем оригинальный метод на декорированный
                setattr(cls, name, wrapper)
        return cls
    return decorator

# Применяем декоратор к классу
@optional_param_decorator(active=True)
class MathOperations:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)  # Рекурсивный вызов

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)  # Рекурсивный вызов

    def sum_numbers(self, a, b):
        return a + b

# Тестирование
print("Факториал (декоратор активен):")
math_ops = MathOperations()
print(math_ops.factorial(5))  # 120

print("\nЧисло Фибоначчи (декоратор активен):")
print(math_ops.fibonacci(5))  # 5

print("\nСумма чисел (декоратор активен):")
print(math_ops.sum_numbers(10, 20))  # 30