n = int(input())

counts = {}

for _ in range(n):
    phone = input().strip()
    counts[phone] = counts.get(phone, 0) + 1

result = 0
for count in counts.values():
    if count == 3:
        result += 1

print(result)