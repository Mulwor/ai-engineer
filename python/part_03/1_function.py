# ================================================================
# ! Функция — блок кода, который выполняется при вызове.
# ! Позволяет избежать дублирования, структурировать код и 
# ! повторно использовать логику.
# ================================================================

# ! ---------- 1. Определение и вызов функции ----------
def greet():
    print("Привет, мир!")

greet()   # вызов, напечатает "Привет, мир!"

# ? Функция с параметром
def greet_person(name):
    print(f"Привет, {name}!")

greet_person("Анна")   # Привет, Анна!

# ? Функция с возвратом значения
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8



# ! ---------- 2. Параметры: позиционные и именованные ----------
# ? Позиционные: порядок важен
def describe_person(name, age, city):
    print(f"{name}, {age} лет, живёт в {city}")

describe_person("Иван", 30, "Москва")

# ? Именованные: указываем имена параметров, порядок не важен
describe_person(age=25, city="СПб", name="Мария")

# ? Смешанный вариант: сначала позиционные, потом именованные
describe_person("Петр", city="Казань", age=40)



# ! ---------- 3. Значения параметров по умолчанию ----------
def greet_with_title(name, title="господин"):
    print(f"Здравствуйте, {title} {name}")

greet_with_title("Иванов")            # господин Иванов
greet_with_title("Петрова", "госпожа") # госпожа Петрова

# ? Важно: значение по умолчанию вычисляется один раз при 
# ? определении функции. Для изменяемых объектов (список, словарь) 
# ? используйте None как default и создавайте внутри.
def bad_append(item, lst=[]):   # НЕПРАВИЛЬНО — список будет общим для всех вызовов
    lst.append(item)
    return lst

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2] — неожиданно!

def correct_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(correct_append(1))   # [1]
print(correct_append(2))   # [2] — теперь правильно

# ! ---------- 4. Переменное число аргументов: *args (позиционные) ----------
# *args собирает все лишние позиционные аргументы в кортеж.

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100

def print_info(name, *args):
    print(f"Имя: {name}, остальное: {args}")

print_info("Алекс", 25, "программист", "Python")   # Имя: Алекс, остальное: (25, 'программист', 'Python')



# ! ---------- 5. Переменное число именованных аргументов: **kwargs ----------
# ? kwargs собирает все лишние именованные аргументы в словарь.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Иван", age=30, city="Москва")
# выведет:
# name = Иван
# age = 30
# city = Москва

def create_user(username, **kwargs):
    user = {"username": username}
    user.update(kwargs)
    return user

user = create_user("alice", email="a@b.com", age=25)
print(user)   # {'username': 'alice', 'email': 'a@b.com', 'age': 25}



# ! ---------- 6. Комбинация параметров ----------
# ? Порядок: позиционные, *args, именованные (со значениями по умолчанию), **kwargs

def complex_func(a, b, *args, c=10, d=20, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}, d={d}")
    print(f"kwargs={kwargs}")

complex_func(1, 2, 3, 4, 5, c=100, e="extra", f=200)
# Вывод:
# a=1, b=2
# args=(3, 4, 5)
# c=100, d=20
# kwargs={'e': 'extra', 'f': 200}



# ! ---------- 7. Распаковка аргументов при вызове ----------
# ? Используйте * для распаковки списка/кортежа в позиционные аргументы
nums = [10, 20]
print(add(*nums))   # 30  (эквивалентно add(10,20))

# Используйте ** для распаковки словаря в именованные аргументы
params = {"age": 30, "city": "Moscow"}
describe_person(name="Олег", **params)   # Олег, 30 лет, живёт в Moscow



# ! ---------- 8. Возврат нескольких значений ----------
# ? Функция может возвращать несколько значений в виде кортежа
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

mn, mx, avg = get_stats([1, 2, 3, 4, 5])
print(f"min={mn}, max={mx}, avg={avg}")



# ! ---------- 9. Области видимости переменных ----------
# ? Локальная переменная существует только внутри функции
def scope_test():
    local_var = 10   # локальная
    print(local_var)

scope_test()
# print(local_var)   # NameError

# Глобальная переменная доступна для чтения внутри функции
global_var = 100
def read_global():
    print(global_var)   # 100

read_global()

# Для изменения глобальной переменной внутри функции используйте global
def change_global():
    global global_var
    global_var = 200

change_global()
print(global_var)   # 200

# Для изменения переменной в объемлющей (nonlocal) функции используйте nonlocal
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)   # "inner"

outer()



# ! ---------- 10. Анонимные функции (lambda) ----------
# ! lambda параметры: выражение - используются для коротких 
# ! операций, часто как аргументы для сортировки, map, filter и т.д.

square = lambda x: x ** 2
print(square(5))   # 25

# Сортировка по ключу (например, по длине строк)
words = ["apple", "banana", "cherry", "date"]
words.sort(key=lambda word: len(word))
print(words)   # ['date', 'apple', 'banana', 'cherry']

# Использование с map и filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)   # [1, 4, 9, 16, 25]
print(evens)     # [2, 4]



# ! ---------- 11. Документирование функций (docstring) ----------
# ! Строка документации — первая строка внутри функции, доступна 
# ! через help() или .__doc__

def multiply(a, b):
    """Умножает два числа и возвращает результат.
    
    Аргументы:
        a (int/float): первый множитель
        b (int/float): второй множитель
    
    Возвращает:
        int/float: произведение a и b
    """
    return a * b

print(multiply.__doc__)   # Выведет docstring
# help(multiply)          # Откроет справку



# ! ---------- 12. Рекурсия ----------
# ? Функция вызывает саму себя. Всегда должно быть условие выхода.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120

# Осторожно: глубокая рекурсия может вызвать RecursionError.
# Для больших глубин используйте итерацию или sys.setrecursionlimit().



# ! ---------- 13. Функции как объекты первого класса ----------
# ? Функции можно присваивать переменным, передавать как аргументы, 
# ? возвращать из функций.

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet_with_style(style_func, name):
    return style_func(f"Привет, {name}!")

print(greet_with_style(shout, "Анна"))   # ПРИВЕТ, АННА!
print(greet_with_style(whisper, "Анна")) # привет, анна!



# ! ---------- 14. Замыкания (closure) ----------
# ? Вложенная функция, которая запоминает переменные из внешней области видимости
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_two = make_multiplier(2)
times_three = make_multiplier(3)
print(times_two(10))   # 20
print(times_three(10)) # 30



# ! ---------- 15. Декораторы (кратко) ----------
# ? Декоратор — функция, которая модифицирует другую функцию.
# ? Часто используется для логирования, измерения времени, проверки прав.

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start:.4f} сек")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Готово!"

print(slow_function())   # Выведет время и результат

# Декораторы могут быть с параметрами, но это уже глубже.



# ! ---------- 16. Аннотации типов (type hints) ----------
# ? Подсказки не влияют на выполнение, но помогают IDE и статическим анализаторам.
def concat(a: str, b: str) -> str:
    return a + b

print(concat("Hello, ", "world!"))   # Hello, world!

# Можно аннотировать и более сложные типы: list[int], dict[str, float] и т.д.
# Для этого импортируйте typing.



# ! ---------- 17. Практический пример: функция для обработки списка с гибкими параметрами ----------
def process_data(data, transform=None, filter_func=None, default=0):
    """
    Применяет преобразование и фильтрацию к данным.
    
    Аргументы:
        data (list): исходный список
        transform (callable, optional): функция преобразования элемента
        filter_func (callable, optional): функция-предикат для фильтрации
        default (any, optional): значение по умолчанию при ошибке
    
    Возвращает:
        list: обработанный список
    """
    if filter_func:
        data = [x for x in data if filter_func(x)]
    if transform:
        data = [transform(x) if x is not None else default for x in data]
    return data

numbers = [1, 2, 3, 4, 5]
processed = process_data(numbers, transform=lambda x: x**2, filter_func=lambda x: x % 2 == 0)
print(processed)   # [4, 16]



# ---------- 18. Важные замечания ----------
# - Функция без return возвращает None.
# - Аргументы передаются по ссылке: если передан изменяемый объект (список, словарь), 
#   его изменения внутри функции влияют на оригинал.
# - Для неизменяемых (числа, строки) изменения внутри функции не влияют на внешнюю переменную.
# - Значения по умолчанию вычисляются один раз — осторожно с изменяемыми типами.
# - Используйте именованные аргументы для улучшения читаемости кода.
# - Документируйте свои функции — это хорошая практика.
# - Не злоупотребляйте глобальными переменными внутри функций.
# - Рекурсию используйте только когда глубина невелика или есть гарантия завершения.
# - Декораторы — мощный инструмент, но начинайте с простых.