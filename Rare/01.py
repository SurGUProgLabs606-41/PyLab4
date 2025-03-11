def validate_args(*expected_types, min_value=None, max_value=None): # Декоратор validate_args для проверки типов и диапазонов аргументов функции
    def decorator(func): # Функция decorator принимает декорируемую функцию func
        def wrapper(*args, **kwargs): # Функция wrapper оборачивает вызов func и выполняет проверки
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)): # Итерирация по аргументам и их ожидаемым типам
                if not isinstance(arg, expected_type): # Проверяем, соответствует ли тип аргумента ожидаемому
                    print(f"Предупреждение: Аргумент {i} не является типом {expected_type}")
                    continue  # Пропуск дальнейшие проверки для этого аргумента

                # Проверка диапазона значений (только для чисел)
                if min_value is not None and arg < min_value:
                    print(f"Предупреждение: Аргумент {i} меньше {min_value}")
                if max_value is not None and arg > max_value:
                    print(f"Предупреждение: Аргумент {i} больше {max_value}")
            return func(*args, **kwargs) # Вызов исходной функции с переданными аргументами
        return wrapper # Возвращение функции wrapper
    return decorator # Возвращение функции decorator

def make_averager():
    numbers = [] # Создаем пустой список для хранения чисел

    @validate_args(int, min_value=0, max_value=100)
    def averager(new_number): # Вложенная функция averager, которая добавляет новое число в список и вычисляет среднее
        numbers.append(new_number) # Добавление нового числа в список
        return sum(numbers) / len(numbers) # Возвращение среднего значения всех чисел в списке

    return averager # Возвращение функции averager (замыкание)

# Пример использования:
avg = make_averager()  # Создание экземпляра функции averager
print(avg(10))  # 10.0
print(avg(20))  # 15.0
print(avg(130))  # 20.0

# Пример использования декоратора validate_args
@validate_args(int, int, min_value=0, max_value=100)  # Ожидание двух аргументов типа int в диапазоне [0, 100]
def add(a, b):
    return a + b # Возвращение сумму двух чисел

print(add(10, 20))  # 30
print(add(-10, 20))  # Предупреждение: Аргумент 0 меньше 0, 10
print(add(110, 20))  # Предупреждение: Аргумент 0 больше 100, 130
#print(add(10, "20"))  # Предупреждение: Аргумент 1 не является типом <class 'int'>, TypeError