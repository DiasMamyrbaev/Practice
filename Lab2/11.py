n, l, r = map(int, input().split())
nums = list(map(int, input().split()))

def reverse_subarray(arr, l, r):
    left = l - 1
    right = r - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(*reverse_subarray(nums, l, r))