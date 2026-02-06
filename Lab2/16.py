n = int(input())
nums = list(map(int, input().split()))
my_set = set()
for i in nums:
    if i in my_set:
        print("NO")    
    else:
        print("YES")
        my_set.add(i)