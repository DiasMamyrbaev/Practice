import sys
from datetime import datetime, timedelta

def parse_moment(s):
    """
    Преобразует строку вида "YYYY-MM-DD UTC±HH:MM" в момент времени UTC,
    соответствующий местной полуночи в указанном часовом поясе.
    """
    parts = s.split()
    date_part = parts[0]
    tz_part = parts[1][3:]  # убираем префикс "UTC"
    year, month, day = map(int, date_part.split('-'))
    sign = 1 if tz_part[0] == '+' else -1
    hh, mm = map(int, tz_part[1:].split(':'))
    offset = sign * (hh * 3600 + mm * 60)  # смещение в секундах

    local_midnight = datetime(year, month, day, 0, 0, 0)
    # UTC = местное - смещение
    return local_midnight - timedelta(seconds=offset)

def main():
    data = sys.stdin.read().strip().splitlines()
    if len(data) < 2:
        return
    t1 = parse_moment(data[0].strip())
    t2 = parse_moment(data[1].strip())
    diff_seconds = abs((t1 - t2).total_seconds())
    days = int(diff_seconds // 86400)  # количество полных дней
    print(days)

if __name__ == "__main__":
    main()