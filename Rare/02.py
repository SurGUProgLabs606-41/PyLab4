# Декоратор для логирования
def log_decorator(func):
    def wrapper(*args, **kwargs): # Функция-обертка, которая принимает произвольные аргументы
        result = func(*args, **kwargs) # Вызов исходной функции func с переданными аргументами и сохранением результата
        print(f"Функция {func.__name__} вызвана с аргументами {args}. Результат: {result}")
        return result # Возвращение результата выполнения исходной функции
    return wrapper # Возвращение функции-обертки

# Функция make_averager создает замыкание для вычисления среднего значения
def make_averager():
    numbers = [] # Создание пустого списка для хранения чисел

    @log_decorator # Применение декоратора log_decorator к функции averager
    def averager(new_number):
        numbers.append(new_number)  # Добавление нового числа в список numbers
        return sum(numbers) / len(numbers) # Возвращение среднего значения всех чисел в списке

    return averager # Возвращение функцию averager (замыкание)

# Пример использования:
avg = make_averager()
print(avg(10))  # 10.0
print(avg(20))  # 15.0
print(avg(30))  # 20.0

#*args позволяет передавать в функцию произвольное количество позиционных аргументов.
#**kwargs позволяет передавать в функцию произвольное количество именованных аргументов (аргументов с ключевыми словами).
#func.__name__ это атрибут функции в Python, который возвращает имя функции в виде строки.
