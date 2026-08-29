# =============================================================
# ! Работа с файлами в Python
# ! Встроенные функции и методы для чтения, записи и управления файлами.
# =============================================================

# ! ---------- 1. Открытие файла: open() ----------
# ? open(file, mode='r', encoding=None, ...) возвращает файловый объект.
# ? Основные режимы (mode):
# ?   'r'  - чтение (по умолчанию), файл должен существовать
# ?   'w'  - запись (создаёт новый или перезаписывает существующий)
# ?   'x'  - эксклюзивное создание, ошибка если файл существует
# ?   'a'  - добавление в конец (если файла нет, создаётся)
# ?   'b'  - бинарный режим (добавляется к основному, например 'rb', 'wb')
# ?   't'  - текстовый режим (по умолчанию)
# ?   '+'  - чтение и запись (например, 'r+', 'w+', 'a+')
# ? Важно: всегда закрывайте файл после работы.
f = open("data.txt", "r")
content = f.read()
f.close()  # обязательно!

# ? Рекомендуется использовать менеджер контекста with (см. раздел 7).


# ! ---------- 2. Чтение из файла ----------
# ? Методы чтения: read(), readline(), readlines().
# ? Для текстовых файлов.

# --- 2.1 read(size=-1) ---
# Читает всё содержимое (или size байт/символов).
with open("file.txt", "r", encoding="utf-8") as f:
    all_text = f.read()
    print(all_text)

# --- 2.2 readline(size=-1) ---
# Читает одну строку до символа новой строки (или size символов).
with open("file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

# --- 2.3 readlines() ---
# Читает все строки и возвращает список строк.
with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# --- 2.4 Итерация по файловому объекту ---
# Удобно читать построчно без загрузки всего файла в память.
with open("big_file.txt", "r") as f:
    for line in f:
        process(line)   # обработать строку


# ! ---------- 3. Запись в файл ----------
# ? Методы записи: write(), writelines().
# ? Режимы 'w' — перезапись, 'a' — добавление, 'x' — эксклюзивное создание.
# ? Для записи строк, а для бинарных — байтовых последовательностей.

# --- 3.1 write(string) ---
# Записывает строку в файл (возвращает количество записанных символов).
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")

# --- 3.2 writelines(iterable) ---
# Записывает список (или любой итерируемый объект) строк.
lines = ["строка 1\n", "строка 2\n", "строка 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# --- 3.3 Добавление в конец (режим 'a') ---
with open("log.txt", "a") as f:
    f.write("Новое сообщение в логе\n")


# ! ---------- 4. Работа с бинарными файлами ----------
# ? Режимы 'rb', 'wb', 'ab', 'rb+', 'wb+', 'ab+'
# ? Чтение/запись байтов (bytes или bytearray).
# ? Чтение: read() возвращает bytes, write(bytes) принимает bytes.

# Запись бинарных данных
data = b'\x00\x01\x02\x03'
with open("binary.bin", "wb") as f:
    f.write(data)

# Чтение бинарных данных
with open("binary.bin", "rb") as f:
    byte_data = f.read()
    print(byte_data.hex())  # 00010203

# Чтение изображения, архива и т.п.


# ! ---------- 5. Позиционирование в файле: tell() и seek() ----------
# ? tell() — текущая позиция в байтах от начала.
# ? seek(offset, whence=0) — перемещает указатель.
# ? whence: 0 — от начала, 1 — от текущей позиции, 2 — от конца.
with open("data.txt", "rb") as f:
    print(f.tell())    # 0
    f.seek(10)         # перейти на 10-й байт от начала
    print(f.tell())    # 10
    f.seek(5, 1)       # сместиться на 5 байт вперёд от текущей позиции
    print(f.tell())    # 15
    f.seek(-3, 2)      # сместиться на 3 байта назад от конца
    print(f.tell())    # размер_файла - 3


# ! ---------- 6. Кодировки (encoding) ----------
# ? Для текстовых файлов важно указывать кодировку (особенно на разных ОС).
# ? По умолчанию используется системная кодировка (может быть проблематично).
# ? Явно указывайте encoding='utf-8' (или 'cp1251', 'latin-1' и т.д.).
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ? При записи тоже указывайте кодировку.
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!")

# ? Ошибка UnicodeDecodeError возникает, если файл в другой кодировке.
# ? Для обработки ошибок используйте параметр errors: 'ignore', 'replace' и др.
with open("file.txt", "r", encoding="ascii", errors="ignore") as f:
    data = f.read()


# ! ---------- 7. Менеджер контекста with ----------
# ? with автоматически закрывает файл (вызывает f.close()) при выходе из блока.
# ? Это гарантирует освобождение ресурсов даже при возникновении исключения.
# ? Рекомендуется всегда использовать with вместо явного close().

# Пример с несколькими файлами:
with open("input.txt", "r") as inf, open("output.txt", "w") as outf:
    for line in inf:
        outf.write(line.upper())

# ? Можно также использовать contextlib.closing для объектов, у которых есть close().


# ! ---------- 8. Проверка существования файла и удаление ----------
# ? Модуль os и pathlib для работы с файловой системой.
import os
import pathlib

# --- os.path.exists ---
if os.path.exists("file.txt"):
    print("Файл существует")

# --- os.remove ---
if os.path.exists("temp.txt"):
    os.remove("temp.txt")   # удалить файл

# --- pathlib (более современный) ---
p = pathlib.Path("file.txt")
if p.exists():
    print("Файл существует")
    p.unlink()   # удалить

# --- os.makedirs / os.rmdir для директорий ---
os.makedirs("new_dir/subdir", exist_ok=True)  # создать папки
os.rmdir("new_dir/subdir")   # удалить пустую папку


# ! ---------- 9. Работа с путями ----------
# ? Используйте os.path.join или pathlib для кросс-платформенности.
import os
from pathlib import Path

# os.path.join
path = os.path.join("folder", "subfolder", "file.txt")

# pathlib
p = Path("folder") / "subfolder" / "file.txt"
print(p)   # folder/subfolder/file.txt (на Windows будет с \)

# ? Получить абсолютный путь: os.path.abspath или Path.resolve().
abs_path = os.path.abspath("file.txt")
abs_path2 = Path("file.txt").resolve()

# ? Получить имя файла, расширение, родительскую директорию.
p = Path("data/archive.zip")
print(p.name)          # archive.zip
print(p.stem)          # archive
print(p.suffix)        # .zip
print(p.parent)        # data

# ? Проверка типа (файл или директория)
p.is_file()   # True/False
p.is_dir()    # True/False


# ! ---------- 10. Дополнительные методы файловых объектов ----------
# ? fileno() — возвращает файловый дескриптор (для низкоуровневых операций).
# ? readable(), writable(), seekable() — проверка режимов.
# ? flush() — принудительная запись буфера на диск (обычно вызывается автоматически).
# ? close() — закрывает файл (после закрытия операции невозможны).
# ? closed — атрибут, указывающий закрыт ли файл.

with open("test.txt", "w") as f:
    print(f.readable())   # False
    print(f.writable())   # True
    f.write("hello")
    f.flush()   # сброс буфера
# после with файл закрыт автоматически


# ! ---------- 11. Работа с временными файлами (tempfile) ----------
# ? Модуль tempfile создаёт временные файлы и директории.
import tempfile

# Создание временного файла (автоматически удаляется при закрытии)
with tempfile.NamedTemporaryFile(mode='w+', delete=True) as tmp:
    tmp.write("временные данные")
    tmp.seek(0)
    print(tmp.read())   # временные данные

# Создание временной директории
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Временная папка: {tmpdir}")
    # файлы внутри будут удалены после выхода из with


# ! ---------- 12. Копирование, перемещение, переименование файлов ----------
# ? Модули shutil и os.
import shutil

# Копирование файла
shutil.copy("source.txt", "dest.txt")          # копирует содержимое и права доступа
shutil.copy2("source.txt", "dest2.txt")        # дополнительно копирует метаданные (время)

# Перемещение / переименование
os.rename("old_name.txt", "new_name.txt")      # переименование
shutil.move("file.txt", "backup/file.txt")     # перемещение с возможным переименованием

# Копирование директории
shutil.copytree("src_dir", "dst_dir")          # рекурсивное копирование


# ! ---------- 13. Чтение и запись больших файлов (по кускам) ----------
# ? Для экономии памяти читайте/пишите блоками, а не целиком.
# ? Используйте read(size) или цикл по файлу.

# Чтение большими блоками (например, по 4096 байт)
with open("bigfile.bin", "rb") as src, open("copy.bin", "wb") as dst:
    while True:
        chunk = src.read(4096)
        if not chunk:
            break
        dst.write(chunk)

# Для текстовых файлов удобно читать построчно:
with open("big.txt", "r") as f:
    for line in f:
        process(line)   # не загружает весь файл в память


# ! ---------- 14. Специализированные модули для работы с форматами ----------
# ? Для CSV: модуль csv
import csv
with open("data.csv", "r", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ? Для JSON: модуль json
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
with open("data.json", "r") as f:
    loaded = json.load(f)

# ? Для XML, YAML, Excel и др. есть сторонние библиотеки (xml, yaml, openpyxl и т.д.)


# ! ---------- 15. Работа с файловыми потоками (sys.stdin, stdout, stderr) ----------
# ? Стандартные потоки доступны как файловые объекты.
import sys
sys.stdout.write("Запись в стандартный вывод\n")
sys.stderr.write("Ошибка\n")
# ? Чтение из stdin:
user_input = sys.stdin.readline()


# ! ---------- 16. Важные замечания и советы ----------
# - Всегда используйте with open(...) as f: — это гарантирует закрытие.
# - Явно указывайте кодировку при работе с текстовыми файлами (UTF-8 предпочтительна).
# - Для бинарных файлов не указывайте encoding.
# - При работе с путями используйте os.path или pathlib, чтобы код был кроссплатформенным.
# - Обрабатывайте возможные исключения: FileNotFoundError, PermissionError, IsADirectoryError и др.
# - Не забывайте про режим 'x' для безопасного создания файла (не перезапишет существующий).
# - Используйте read() осторожно для больших файлов, чтобы не переполнить память.
# - Для построчного чтения больших файлов используйте итератор по файлу (for line in f).
# - flush() полезен, когда нужно гарантировать запись до закрытия (например, логирование).
# - В режиме 'r+' можно читать и писать, но позиция указателя важна.
# - Для работы с архивами (zip, tar) используйте модули zipfile, tarfile.
# - Для записи объектов Python (сериализация) используйте pickle, но будьте осторожны с безопасностью.