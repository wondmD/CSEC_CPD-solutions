n = input()
s= "47"
c = 0
for i in n:
    if i == "4" or i == '7':
        c+=1
t = True
for i in str(c):
    if i not in s:
        t = False
        break
if t:
    print("YES")
else:
    print("NO")