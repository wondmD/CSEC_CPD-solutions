k,n,w = map(int, input().split())
tot = (w*2*k + w*w*k - k*w)//2
if tot <= n :
    print(0)
else :
    print (tot-n) 