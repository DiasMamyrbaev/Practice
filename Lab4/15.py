import sys
from datetime import datetime, timedelta

def parse_date_tz(line):
    # Example: 2000-05-10 UTC+02:00
    parts = line.split()
    date_str = parts[0]
    tz_str = parts[1].replace('UTC', '')
    
    # Parse offset (handle + or -)
    sign = 1 if tz_str[0] == '+' else -1
    hours = int(tz_str[1:3])
    minutes = int(tz_str[4:6])
    offset_seconds = sign * (hours * 3600 + minutes * 60)
    
    # Create datetime object for local midnight
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Convert to UTC timestamp (Local - Offset)
    return dt.timestamp() - offset_seconds, dt.month, dt.day, offset_seconds

def solve():
    lines = sys.stdin.readlines()
    if not lines: return
    
    # Get Birth info and Current info
    birth_utc, b_month, b_day, b_offset = parse_date_tz(lines[0].strip())
    curr_utc, _, _, _ = parse_date_tz(lines[1].strip())
    
    # Current date in local time to determine the year
    curr_local_dt = datetime.fromtimestamp(curr_utc + 0) # Use a dummy for year extraction
    # Better: just use the year from the input string directly
    curr_year = int(lines[1].split('-')[0])

    # Try birthday in current year, then next year
    for year in [curr_year, curr_year + 1]:
        target_month, target_day = b_month, b_day
        
        # Leap year adjustment
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if target_month == 2 and target_day == 29 and not is_leap:
            target_day = 28
            
        try:
            bday_local = datetime(year, target_month, target_day)
            bday_utc = bday_local.timestamp() - b_offset
            
            delta = bday_utc - curr_utc
            
            if delta >= 0:
                # Formula: ceil(delta / 86400)
                # In Python, -(-a // b) is ceiling division
                days_left = -(-int(delta) // 86400)
                print(days_left)
                return
        except ValueError:
            continue

solve()