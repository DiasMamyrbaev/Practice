from datetime import datetime

dt = datetime.now()

dt_no_microseconds = dt.replace(microsecond=0)

print(dt_no_microseconds)