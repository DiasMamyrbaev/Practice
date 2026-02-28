from datetime import datetime

date_start = datetime(2023, 10, 1, 12, 0, 0)
date_end = datetime.now()

difference = date_end - date_start

seconds_diff = difference.total_seconds()

print(date_end.replace(microsecond=0))
print(f"{int(seconds_diff)}")