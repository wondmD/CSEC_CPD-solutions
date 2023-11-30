n, m= map(int, input().split())
l = list(map(int, input().split()))[:n]
l.sort()
out = 0
c = 0
for i in range(n):
    if c >= m:
        break
    if l[i] < 0:
        out += abs(l[i])
        c+=1
    else:
        break
print (out)