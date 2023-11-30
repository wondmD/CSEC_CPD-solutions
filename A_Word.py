st = input()
c = 0
x = 0
for i in st:
    if i == i.lower():
        c += 1
    if c >= len(st)/2:
        x += 1
        break
if x == 1:
    print (st.lower())
else :
    print(st.upper())