# Декоратор - это патерн программирования, который позволяет
# добавлять новый функционал к нашей функции, не видоизменяя 
# саму функцию

def logger(func):
    def wrapper():
        print("Начинаю работу...")   # Добавили поведение ДО
        func()                      # Запускаем оригинальную функцию
        print("Заканчиваю работу...") # Добавили поведение ПОСЛЕ
    return wrapper

@logger
def say_hello():
    print("Привет!")


# ==================================================================

class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Получает класс, может создавать объекты
        age = 2026 - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        # Просто функция внутри класса, не зависит от класса/объекта
        return age >= 18

# Использование
p1 = Person.from_birth_year("John", 1995)  # classmethod создал объект
print(p1.age)  # 31

print(Person.is_adult(20))  # True (staticmethod — просто хелпер)