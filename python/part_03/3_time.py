# ================================================================
# Работа с датами и временем в Python (модуль datetime)
# Модуль datetime — стандартный, не требует установки.
# Позволяет: получать текущую дату/время, создавать свои даты,
# вычислять разницу между датами, форматировать и парсить строки.
# ================================================================

# ---------- 1. Импорт модуля ----------
# Вариант 1: импорт всего модуля
import datetime
now = datetime.datetime.now()   # обращение через префикс datetime

# Вариант 2: импорт конкретных классов (рекомендуется)
from datetime import datetime, date, time, timedelta, timezone

# Вариант 3: импорт всех имён (не рекомендуется, может вызвать конфликты)
# from datetime import *

# ---------- 2. Основные классы модуля datetime ----------
# date      — только дата (год, месяц, день)
# time      — только время (час, минута, секунда, микросекунда)
# datetime  — дата + время
# timedelta — разница между двумя датами/временами (интервал)
# tzinfo    — информация о часовом поясе (абстрактный класс)
# timezone  — реализация часового пояса с фиксированным смещением

# ---------- 3. Класс date — работа с датами ----------
from datetime import date

# Создание конкретной даты
d1 = date(2025, 12, 31)          # 31 декабря 2025 года
print(d1)                         # 2025-12-31

# Получить текущую дату
today = date.today()
print(today)                      # 2026-08-24 (пример)

# Создать дату из timestamp (количество секунд с 01.01.1970)
from_timestamp = date.fromtimestamp(1609459200)  # 2021-01-01
print(from_timestamp)

# Атрибуты объекта date
print(d1.year)   # 2025
print(d1.month)  # 12
print(d1.day)    # 31

# День недели: 0 = понедельник, 6 = воскресенье
print(d1.weekday())    # 2 (среда)
# ISO день недели: 1 = понедельник, 7 = воскресенье
print(d1.isoweekday()) # 3

# Замена части даты (возвращает новый объект)
d2 = d1.replace(year=2026)
print(d2)              # 2026-12-31

# ---------- 4. Класс time — работа со временем ----------
from datetime import time

t1 = time(14, 30, 15, 500000)   # 14:30:15.500000
print(t1)                        # 14:30:15.500000

# Атрибуты
print(t1.hour)    # 14
print(t1.minute)  # 30
print(t1.second)  # 15
print(t1.microsecond)  # 500000

# Создание времени без microseconds
t2 = time(9, 0, 0)
print(t2)          # 09:00:00

# ---------- 5. Класс datetime — дата и время вместе ----------
from datetime import datetime

# Создание конкретной даты и времени
dt1 = datetime(2025, 6, 15, 10, 30, 0, 123456)
print(dt1)          # 2025-06-15 10:30:00.123456

# Текущие дата и время
now = datetime.now()
print(now)          # 2026-08-24 14:30:45.123456

# datetime.today() — аналогично now(), но без поддержки часовых поясов
now_alt = datetime.today()
print(now_alt)      # 2026-08-24 14:30:45.123456

# Комбинирование date и time в datetime
d = date(2025, 12, 25)
t = time(18, 0, 0)
dt2 = datetime.combine(d, t)
print(dt2)          # 2025-12-25 18:00:00

# Извлечение компонентов
print(now.year)     # 2026
print(now.month)    # 8
print(now.day)      # 24
print(now.hour)     # 14
print(now.minute)   # 30
print(now.second)   # 45

# Преобразование datetime в date и time
only_date = now.date()    # date(2026, 8, 24)
only_time = now.time()    # time(14, 30, 45, 123456)

# ---------- 6. Класс timedelta — разница между датами ----------
from datetime import timedelta

# Создание интервала
delta = timedelta(days=5, hours=3, minutes=30)
print(delta)         # 5 days, 3:30:00

# Арифметика с датами
today = date.today()
future = today + timedelta(days=10)
past = today - timedelta(days=7)
print(future)        # дата через 10 дней
print(past)          # дата 7 дней назад

# Разница между двумя датами
d1 = date(2025, 12, 31)
d2 = date(2026, 1, 15)
diff = d2 - d1
print(diff)          # 15 days, 0:00:00
print(diff.days)     # 15

# timedelta с datetime
now = datetime.now()
in_2_hours = now + timedelta(hours=2)
yesterday = now - timedelta(days=1)
print(in_2_hours)
print(yesterday)

# total_seconds() — общее количество секунд в интервале
delta = timedelta(days=1, hours=2, minutes=30)
print(delta.total_seconds())   # 95400.0

# ---------- 7. Форматирование дат: strftime() ----------
# strftime = string format time — преобразует объект datetime в строку
# Основные директивы (коды форматирования):
# %Y — год (4 цифры)       %y — год (2 цифры)
# %m — месяц (01-12)       %d — день (01-31)
# %H — час (00-23)         %I — час (01-12)
# %M — минуты (00-59)      %S — секунды (00-59)
# %A — полное название дня  %a — сокращённое название дня
# %B — полное название месяца  %b — сокращённое название месяца
# %p — AM/PM                %f — микросекунды (6 цифр)
# %j — день года (001-366)  %U — номер недели в году

now = datetime.now()
print(now.strftime("%Y-%m-%d"))              # 2026-08-24
print(now.strftime("%d/%m/%Y"))              # 24/08/2026
print(now.strftime("%H:%M:%S"))              # 14:30:45
print(now.strftime("%A, %d %B %Y"))          # Monday, 24 August 2026
print(now.strftime("%I:%M %p"))              # 02:30 PM
print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))  # 2026-08-24 14:30:45.123456
print(now.strftime("%j"))                    # 236 (день года)

# ---------- 8. Парсинг строк в даты: strptime() ----------
# strptime = string parse time — преобразует строку в объект datetime
# Второй аргумент — формат строки (те же директивы, что в strftime)

date_str = "25-12-2025 15:30:00"
parsed = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(parsed)          # 2025-12-25 15:30:00

date_str2 = "2026/08/24"
parsed2 = datetime.strptime(date_str2, "%Y/%m/%d")
print(parsed2)         # 2026-08-24 00:00:00

# ISO-формат: fromisoformat() и isoformat()
iso_str = "2026-08-24T14:30:45"
dt_iso = datetime.fromisoformat(iso_str)
print(dt_iso)          # 2026-08-24 14:30:45
print(dt_iso.isoformat())  # 2026-08-24T14:30:45

# ---------- 9. Часовые пояса (timezone) ----------
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo   # Python 3.9+

# Создание часового пояса с фиксированным смещением
tz_utc3 = timezone(timedelta(hours=3))
dt_with_tz = datetime(2026, 8, 24, 14, 30, tzinfo=tz_utc3)
print(dt_with_tz)      # 2026-08-24 14:30:00+03:00

# Текущее время в UTC
utc_now = datetime.now(timezone.utc)
print(utc_now)         # 2026-08-24 11:30:45.123456+00:00

# Текущее время с учётом часового пояса (Python 3.9+)
# Для установки: pip install tzdata (если нет zoneinfo)
try:
    moscow_tz = ZoneInfo("Europe/Moscow")
    moscow_now = datetime.now(moscow_tz)
    print(moscow_now)  # 2026-08-24 14:30:45.123456+03:00
except Exception:
    print("Для работы с zoneinfo установите пакет tzdata")

# Преобразование между часовыми поясами
utc_dt = datetime(2026, 8, 24, 10, 0, 0, tzinfo=timezone.utc)
ny_tz = ZoneInfo("America/New_York")
ny_dt = utc_dt.astimezone(ny_tz)
print(ny_dt)           # 2026-08-24 06:00:00-04:00

# ---------- 10. Полезные методы и функции ----------
from datetime import datetime

# Сравнение дат
d1 = date(2025, 1, 1)
d2 = date(2025, 12, 31)
print(d1 < d2)         # True
print(d1 == d2)        # False

# Минимальная и максимальная дата
print(date.min)        # 0001-01-01
print(date.max)        # 9999-12-31

# Получить timestamp (Unix-время)
now = datetime.now()
ts = now.timestamp()
print(ts)              # 1692877845.123456

# Создать datetime из timestamp
dt_from_ts = datetime.fromtimestamp(1692877845)
print(dt_from_ts)

# Замена части даты/времени (возвращает новый объект)
dt = datetime(2025, 6, 15, 10, 30)
dt_new = dt.replace(year=2026, hour=12)
print(dt_new)          # 2026-06-15 12:30:00

# ---------- 11. Примеры из реальной жизни ----------

# Пример 1: Сколько дней до Нового года?
today = date.today()
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"До Нового года осталось {days_left} дней")

# Пример 2: Возраст по дате рождения
birthday = date(1995, 5, 15)
today = date.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
print(f"Возраст: {age} лет")

# Пример 3: Напоминание за 30 минут до встречи
meeting = datetime(2026, 8, 25, 15, 0, 0)
reminder = meeting - timedelta(minutes=30)
print(f"Напоминание в: {reminder.strftime('%H:%M')}")  # 14:30

# Пример 4: Генерация списка дат за последние 7 дней
today = date.today()
last_week = [today - timedelta(days=i) for i in range(7)]
for d in sorted(last_week):
    print(d.strftime("%A, %d.%m.%Y"))

# Пример 5: Парсинг дат из логов
log_line = "2026-08-24 14:30:45 ERROR Something went wrong"
log_date = datetime.strptime(log_line[:19], "%Y-%m-%d %H:%M:%S")
print(f"Ошибка произошла: {log_date}")

# ---------- 12. Важные замечания ----------
# - Модуль datetime встроен в Python, не требует установки.
# - Для сложных операций с часовыми поясами используйте zoneinfo (Python 3.9+)
#   или стороннюю библиотеку pytz.
# - timedelta поддерживает: days, seconds, microseconds, milliseconds,
#   minutes, hours, weeks.
# - Не путайте strftime (datetime -> строка) и strptime (строка -> datetime).
# - Для работы только с датами используйте date, только со временем — time.
# - Все объекты datetime immutable — методы replace/create возвращают новые.
# - При работе с БД (SQLite, PostgreSQL) используйте ISO-формат.
# - Для больших объёмов данных рассмотрите pandas (обработка временных рядов).