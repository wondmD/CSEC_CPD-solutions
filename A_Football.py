s = input()
p1 = 0
p2 = 1
x= "NO"
while p2 < len(s):
    if s[p1] == s[p2]:
        p2 +=1
    else :
        p1+=1
    if p2 - p1 >= 7:
        x = "YES"
        break
print(x)