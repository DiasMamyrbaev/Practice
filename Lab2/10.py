n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr, reverse = True)
print(*arr2)