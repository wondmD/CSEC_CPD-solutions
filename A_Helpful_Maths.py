ls = list(map(int, input().split("+")))
if len(ls) > 1:
    ls.sort()
    s = ""
    for i in ls:
        s+= str(i)
        s+= "+"
    print (s[:-1])
else :
    print (str(ls[0]))