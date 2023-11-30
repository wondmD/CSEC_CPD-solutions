n = int(input())
clrs = input()

c = 0
for i in range(n-1):
    if clrs[i] == clrs[i+1]:
        c += 1
print(c)