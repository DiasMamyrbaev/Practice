n = int(input()) 
arr = list(map(int, input().split()))

unique_numbers = sorted(set(arr))

most_frequent = unique_numbers[0]
max_count = 0

for num in unique_numbers:
    current_count = arr.count(num)
    if current_count > max_count:
        max_count = current_count
        most_frequent = num

print(most_frequent)