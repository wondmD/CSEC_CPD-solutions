n = int(input())
v = ""
for i in range(2, n+1, 2):
    if (n-i)%2 ==0:
        v+="YES"
        break
if v != "" and n>=4:
    print (v)
else :
    print ("NO")