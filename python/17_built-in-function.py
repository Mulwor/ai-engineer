# ================================================================
# ! Встроенные функции Python (Built-in Functions)
# ! Это функции, которые всегда доступны в интерпретаторе и 
# ! не требуют импорта. Полный список и детали: docs.python.org/library/functions.html
# ================================================================
# ! ---------- 1. Работа с числами ----------
# ? abs() - абсолютное значение (модуль числа)[reference:2]
print(abs(-5))          # 5
print(abs(3+4j))        # 5.0 (модуль комплексного числа)

# ? round() - округление числа
print(round(3.14159, 2))  # 3.14
print(round(3.5))         # 4 (банковское округление к ближайшему чётному)

# ? pow() - возведение в степень (аналог **, но с поддержкой mod)
print(pow(2, 3))          # 8
print(pow(2, 3, 5))       # 3 (2^3 % 5)

# ? divmod() - возвращает кортеж (частное, остаток)[reference:3]
quotient, remainder = divmod(10, 3)
print(quotient, remainder)  # 3 1

# ? sum() - сумма элементов итерируемого объекта
print(sum([1, 2, 3, 4]))    # 10
print(sum([1, 2, 3], 10))   # 16 (с начальным значением)

# ? max() / min() - максимум и минимум
print(max([1, 5, 2, 8]))    # 8
print(min(10, 20, 5, 30))   # 5
print(max("hello"))         # 'o' (по алфавиту)



# ! ---------- 2. Преобразование типов ----------
# ? int() - преобразование в целое число[reference:4]
print(int("42"))            # 42
print(int(3.99))            # 3
print(int("FF", 16))        # 255 (из шестнадцатеричной)

# ? float() - преобразование в число с плавающей точкой[reference:5]
print(float("3.14"))        # 3.14
print(float(42))            # 42.0

# ? str() - преобразование в строку
print(str(42))              # "42"
print(str([1, 2, 3]))       # "[1, 2, 3]"

# ? bool() - преобразование в булево значение[reference:6]
print(bool(0))              # False
print(bool("hello"))        # True
print(bool([]))             # False

# ? list() - преобразование в список
print(list("abc"))          # ['a', 'b', 'c']
print(list((1, 2, 3)))      # [1, 2, 3]

# ? tuple() - преобразование в кортеж
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(tuple("abc"))         # ('a', 'b', 'c')

# ? dict() - создание словаря[reference:7]
print(dict(a=1, b=2))       # {'a': 1, 'b': 2}
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# ? set() - создание множества
print(set([1, 2, 2, 3]))    # {1, 2, 3}
print(set("hello"))         # {'h', 'e', 'l', 'o'}

# ? frozenset() - неизменяемое множество[reference:8]
fs = frozenset([1, 2, 3])
# fs.add(4)  # Ошибка! frozenset неизменяем

# ? chr() / ord() - преобразование между символом и его кодом Unicode[reference:9]
print(chr(65))              # 'A'
print(ord('A'))             # 65

# ? bin() / oct() / hex() - преобразование в двоичную, восьмеричную, шестнадцатеричную[reference:10]
print(bin(42))              # '0b101010'
print(oct(42))              # '0o52'
print(hex(42))              # '0x2a'



# ! ---------- 3. Работа с последовательностями и итераторами ----------
# ? len() - длина последовательности[reference:11]
print(len("hello"))         # 5
print(len([1, 2, 3]))       # 3

# ? range() - генератор числовой последовательности
for i in range(5):
    print(i, end=' ')       # 0 1 2 3 4
print()
for i in range(2, 10, 2):
    print(i, end=' ')       # 2 4 6 8

# ? enumerate() - возвращает пары (индекс, значение)[reference:12]
for idx, val in enumerate(['a', 'b', 'c']):
    print(idx, val)         # 0 a, 1 b, 2 c
for idx, val in enumerate(['a', 'b', 'c'], start=1):
    print(idx, val)         # 1 a, 2 b, 3 c

# ? zip() - объединяет несколько последовательностей в кортежи
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ? reversed() - возвращает обратный итератор
for i in reversed([1, 2, 3]):
    print(i, end=' ')       # 3 2 1
print()
print(list(reversed("hello")))  # ['o', 'l', 'l', 'e', 'h']

# ? sorted() - возвращает отсортированный список[reference:13]
print(sorted([3, 1, 4, 2]))     # [1, 2, 3, 4]
print(sorted("hello"))          # ['e', 'h', 'l', 'l', 'o']
print(sorted([3, 1, 4, 2], reverse=True))  # [4, 3, 2, 1]

# ? slice() - создание объекта среза
s = slice(1, 5, 2)
print("hello"[s])           # 'el' (индексы 1 и 3)

# ? iter() / next() - работа с итераторами[reference:14]
it = iter([1, 2, 3])
print(next(it))             # 1
print(next(it))             # 2
print(next(it))             # 3
# print(next(it))           # StopIteration

# ? all() / any() - проверка всех или хотя бы одного 
# ? элемента[reference:15][reference:16]
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(any([False, False, True])) # True
print(any([False, False, False]))# False

# ? filter() - фильтрация элементов по условию[reference:17]
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                # [2, 4, 6]

# ? map() - применение функции к каждому элементу
squared = list(map(lambda x: x**2, numbers))
print(squared)              # [1, 4, 9, 16, 25, 36]



# ! ---------- 4. Работа с объектами и атрибутами ----------
# ? type() - возвращает тип объекта[reference:18]
print(type(42))             # <class 'int'>
print(type("hello"))        # <class 'str'>

# ? isinstance() - проверка принадлежности к типу
print(isinstance(42, int))  # True
print(isinstance("hello", (int, str)))  # True

# ? issubclass() - проверка, является ли класс подклассом[reference:19]
class Parent: pass
class Child(Parent): pass
print(issubclass(Child, Parent))  # True

# ? id() - уникальный идентификатор объекта[reference:20]
print(id("hello"))          # 123456789 (число)

# ? hash() - хеш-значение объекта (если объект хешируемый)
print(hash("hello"))        # -123456789 (число)

# ? dir() - список атрибутов и методов объекта[reference:21]
print(dir([]))              # ['__add__', '__class__', ...]

# ? getattr() / setattr() / hasattr() / delattr() - 
# ? работа с атрибутами[reference:22][reference:23]
class Person:
    name = "Alice"
p = Person()
print(getattr(p, "name"))   # "Alice"
setattr(p, "name", "Bob")
print(p.name)               # "Bob"
print(hasattr(p, "age"))    # False
delattr(p, "name")
# print(p.name)             # AttributeError

# ? callable() - проверяет, можно ли вызвать объект как функцию[reference:24]
print(callable(print))      # True
print(callable(42))         # False

# ? property() - создание свойства (используется в классах)
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32
    fahrenheit = property(get_fahrenheit)

t = Temperature(25)
print(t.fahrenheit)         # 77.0



# ! ---------- 5. Ввод/вывод и отладка ----------
# ? print() - вывод в консоль[reference:25]
print("Hello, world!")
print(1, 2, 3, sep='-')     # 1-2-3
print("Hello", end='!\n')   # Hello!

# ? input() - ввод с клавиатуры[reference:26]
# * name = input("Введите имя: ")
# * print(f"Привет, {name}!")

# ? breakpoint() - вызывает отладчик (Python 3.7+)[reference:27]
# ? breakpoint()  # Остановит выполнение и откроет отладчик



# ! ---------- 6. Динамическое выполнение кода ----------
# ? eval() - выполняет строку как выражение Python[reference:28]
x = 5
print(eval("x * 2"))        # 10
print(eval("sum([1, 2, 3])"))  # 6

# ? exec() - выполняет блок кода Python[reference:29]
code = """
def hello():
    print("Hello from exec!")
hello()
"""
exec(code)                  # Hello from exec!

# ? compile() - компилирует код в объект для последующего 
# ? выполнения[reference:30]
code_obj = compile("print('Hello')", '<string>', 'exec')
exec(code_obj)              # Hello



# ! ---------- 7. Работа с классами и методами ----------
# ? classmethod() - создаёт классовый метод[reference:31]
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Вызван классовый метод класса {cls.__name__}")
MyClass.class_method()      # Вызван классовый метод класса MyClass

# ? staticmethod() - создаёт статический метод
class MyClass:
    @staticmethod
    def static_method():
        print("Статический метод")
MyClass.static_method()     # Статический метод

# ? super() - доступ к методам родительского класса
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
c = Child()
c.greet()                   # Hello from Parent
                            # Hello from Child

# ? object() - создаёт простой объект
obj = object()
# ? print(obj)  # <object object at 0x...>



# ! ---------- 8. Специализированные функции ----------
# ? memoryview() - представление буфера памяти без 
# ? копирования[reference:32]
data = bytearray(b'hello')
mv = memoryview(data)
print(mv[0])                # 104 (код символа 'h')
mv[0] = 72                  # меняем 'h' на 'H'
print(data)                 # bytearray(b'Hello')

# ? repr() - строковое представление объекта для отладки[reference:33]
print(repr("hello"))        # "'hello'"
print(repr([1, 2, 3]))      # "[1, 2, 3]"

# ? ascii() - repr() с экранированием не-ASCII символов[reference:34]
print(ascii("Привет"))      # "'\\u041f\\u0440\\u0438\\u0432\\u0435\\u0442'"

# ? format() - форматирование значения[reference:35]
print(format(42, 'b'))      # '101010' (двоичное)
print(format(42, 'x'))      # '2a' (шестнадцатеричное)

# ? vars() - возвращает словарь атрибутов объекта
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Alice", 30)
print(vars(p))              # {'name': 'Alice', 'age': 30}

# ? locals() / globals() - доступ к локальным и глобальным переменным
x = 10
def test():
    y = 20
    print(locals())         # {'y': 20}
test()
print(globals()['x'])       # 10

# ! ---------- 9. Асинхронные функции (Python 3.10+) ----------
# ? aiter() - возвращает асинхронный итератор[reference:36]
# ? anext() - возвращает следующий элемент асинхронного итератора[reference:37]
# ? Эти функции используются в асинхронном коде с async/await.



# ---------- 10. Важные замечания ----------
# - Встроенные функции всегда доступны без импорта.
# - Некоторые "функции" (например, int, str, list) на самом деле являются классами.
# - Для получения полного списка используйте dir(__builtins__).
# - Многие встроенные функции можно переопределить, но делать это не рекомендуется.
# - Все встроенные функции документированы в официальной документации Python.

# Получение списка всех встроенных имён
import builtins
print(len(dir(builtins)))   # Количество встроенных имён