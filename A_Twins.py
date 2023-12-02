n = int(input())
l = list(map(int, input().split()))[:n]
tot = sum(l)
l.sort(reverse=True)
s = 0
c = 0
for i in range(n):
    if s > tot/2:
        break
    else:
        s += l[i]
        c += 1
print (c)
