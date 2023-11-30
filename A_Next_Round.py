n , k = map(int, input().split())
scores = list(map(int, input().split()))
c = 0
for i in range(len(scores)):
    if scores[i] >0 and scores[i] >= scores[k-1]:
        c+=1
print(c)