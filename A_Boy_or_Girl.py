name = input()
v = ""
for i in name:
    if i not in v:
        v+=i
n = len(v)
if n%2 == 0:
    print ("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
