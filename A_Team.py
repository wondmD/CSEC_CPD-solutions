c = 0
for i in range(int(input())):
    if sum(list(map(int, input().split()))) >= 2:
        c+=1
print (c)