n = int(input())
vals = list(map(int, input().split()))[:n]
ps = [0] * n
ps[0] = vals[0]
for i in range(1,n):
    ps[i] =  ps[i-1] + vals[i]
vals.sort()
psor = [0] * n
psor[0] = vals[0]
for i in range(1,n):
    psor[i] =  psor[i-1] + vals[i]

n2 = int(input())
for i in range(n2):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if q[1] > 1:
            print(ps[q[2]-1] - ps[q[1]-2])
        else:
            print(ps[q[2]-1] )
    else:
        if q[1] >1:
            print(psor[q[2]-1] - psor[q[1]-2])
        else :
            print(psor[q[2]-1])