arr = list(map(int, input().rstrip().split()))
result =[]
for i in range(100):
    result.append(0)
for i in arr :
    result[i] +=1
for i in result:
    print(i,end=" ")