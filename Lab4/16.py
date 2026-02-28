import sys
from datetime import datetime, timezone, timedelta

def get_utc_seconds(line):
    # Разрезаем строку: Дата, Время, Пояс
    parts = line.split()
    date_str = f"{parts[0]} {parts[1]}"
    tz_str = parts[2].replace("UTC", "") # Получаем "+03:00"
    
    # Парсим время как "наивное" (без зоны)
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    
    # Определяем смещение
    sign = 1 if tz_str[0] == '+' else -1
    hours = int(tz_str[1:3])
    minutes = int(tz_str[4:6])
    
    # Создаем объект временной зоны
    offset = timedelta(hours=hours, minutes=minutes)
    if sign == -1:
        offset = -offset
    
    # Привязываем зону к времени
    dt_with_tz = dt.replace(tzinfo=timezone(offset))
    
    # timestamp() возвращает количество секунд с 1 января 1970 года UTC
    return int(dt_with_tz.timestamp())

# Считываем данные
lines = sys.stdin.readlines()
start_total_seconds = get_utc_seconds(lines[0].strip())
end_total_seconds = get_utc_seconds(lines[1].strip())

# Результат — простая разница
print(end_total_seconds - start_total_seconds)