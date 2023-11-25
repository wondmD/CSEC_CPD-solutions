arr = list(map(int, input().split()))
tot = 0
n = len(arr)
win = 1
while win <= n:
    left = 0
    right = win
    while right <= n:
        if right == n:
            print(arr[left:])
            tot += sum(arr[left:])
            left+=1
            right+=1
            continue
        print(arr[left:right])
        tot += sum(arr[left:right])
        left+=1
        right+=1
    win +=2
print (tot)