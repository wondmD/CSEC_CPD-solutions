def max_sum_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    curr_sum = 0
    for i in range(n):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum
results = []
t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    for i in range(n - 1):
        if arr[i] % 2 != arr[i + 1] % 2:
            new_arr.append(arr[i])
    new_arr.append(arr[n - 1])
    result = max_sum_subarray(new_arr)
    results.append(result)

for i in results:
    print(i)