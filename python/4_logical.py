# =====================================================
# ! Логические операторы (Boolean operators)
# =====================================================

# Базовые: not, and, or
isAdult = True
isNotTrue = not True          # False
isAdult = False               # переопределяем
isNotFalse = not False        # True

print("not True =", not True)        # False
print("not False =", not False)      # True
print("True and False =", True and False)   # False
print("True or False =", True or False)     # True


# =====================================================
# ! Важно: возвращаемые значения and / or (short-circuit)
# =====================================================
# ! and возвращает первое ложное значение (falsy) или последнее истинное (truthy)
# ! or  возвращает первое истинное значение (truthy) или последнее ложное (falsy)

print("0 and 2 =", 0 and 2)          # 0 (0 — falsy, результат сразу)
print("2 and 3 =", 2 and 3)          # 3 (оба truthy → возвращается последнее)
print("0 or 2 =", 0 or 2)            # 2 (0 — falsy, возвращается первое truthy)
print("0 or False =", 0 or False)    # False (оба falsy → последнее)

# ? Это часто используют для значений по умолчанию:
default = None or "default_value"    # "default_value"


# =====================================================
# ! Сравнения и числовой эквивалент True/False
# =====================================================

# ? True == 1, False == 0 (но это не одно и то же!)
print("True + True =", True + True)   # 2
print("True * 8 =", True * 8)         # 8
print("False - 5 =", False - 5)       # -5

# ? Операторы сравнения: ==, !=, >, <, >=, <=
print("0 == False =", 0 == False)     # True (числовое равенство)
print("2 > True =", 2 > True)         # True (2 > 1)
print("2 == True =", 2 == True)       # False (2 != 1)
print("-5 != False =", -5 != False)   # True (-5 != 0)

# ? Оператор is проверяет идентичность объектов, а не равенство значений
# ? (полезно для None, True, False и других синглтонов)
print("True is True =", True is True)   # True
print("1 is True =", 1 is True)         # False (разные объекты)


# =====================================================
# ! Приоритет логических операторов
# =====================================================

# Приоритет (от высшего к низшему): not > and > or
# Пример: not True and False or True
# → сначала not True → False,
# → затем False and False → False,
# → затем False or True → True
print("not True and False or True =", not True and False or True)   # True

# Для ясности лучше использовать скобки:
print("(not True) and (False or True) =", (not True) and (False or True))   # False


# =====================================================
# ! Цепочки сравнений (chained comparisons)
# =====================================================

# Python позволяет записывать сравнения цепочкой (как в математике)
x = 5
print("1 < x < 10 =", 1 < x < 10)          # True (эквивалентно 1 < x and x < 10)
print("x < 3 or x > 7 =", x < 3 or x > 7)  # False

# Будьте осторожны при сравнении разных типов (в Python 3 — ошибка)
# print(3 < '5')  # TypeError


# =====================================================
# ! Falsy и Truthy значения (приведение к bool)
# =====================================================

# ! None, 0, пустые строки/списки/словари/кортежи/множества → False
# Все остальные значения → True
print("bool(0) =", bool(0))          # False
print("bool('') =", bool(""))        # False
print("bool([]) =", bool([]))        # False
print("bool({}) =", bool({}))        # False
print("bool(()) =", bool(()))        # False
print("bool(set()) =", bool(set()))  # False
print("bool(4) =", bool(4))          # True
print("bool(-6) =", bool(-6))        # True


# =====================================================
# ! Логические операторы с числами (полезные трюки)
# =====================================================

# Пример: выбор значения по умолчанию
name = "" or "Anonymous"   # если name falsy, берём "Anonymous"
print("name =", name)      # "Anonymous"

# Пример: вычисление, если значение истинно
value = 10
result = value and value * 2   # если value truthy → value * 2, иначе value
print("result =", result)      # 20

# ! Не путайте with побитовыми операторами &, |, ^, ~
# (у них другой приоритет и они работают на уровне бит)