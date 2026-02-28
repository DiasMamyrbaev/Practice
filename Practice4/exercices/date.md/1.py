from datetime import datetime, timedelta

now = datetime.now()

five_days_ago = now - timedelta(days=5)

print(five_days_ago)