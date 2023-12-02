tc = list(map(int, input().split()))
rcps = []
ad = tc[1]
for i in range(tc[0]):
    x= []
    rcps.append(list(map(int, input().split())))
ll = []
for i in range(tc[2]):
    ll.append(list(map(int, input().split())))

a = ll[0][0]
b = ll[-1][0]
dic = {}
c = 0
for j in rcps:
    x, y = j[0], j[1]
    v = 0
    for k in range(a, b+1):
        if x<=k and k<=y:
            if not k in dic.keys():
                dic[k] = 1
            else:
                c+=1
    print(c)