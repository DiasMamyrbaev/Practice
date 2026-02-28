# Date and time operations
from datetime import datetime, date, time, timedelta, timezone

# Текущая дата и время
now = datetime.now()
print(now)

# Создание конкретной даты
some_date = date(2025, 12, 31)
print(some_date)

# Форматирование
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Разбор строки
parsed = datetime.strptime("2025-01-01 12:00", "%Y-%m-%d %H:%M")
print(parsed)

# Разница между датами
delta = parsed - now
print(delta.days)

# Часовые пояса
utc_now = datetime.now(timezone.utc)
print(utc_now)