x= 0
for i in range(int(input())):
    prgrm = input()
    if prgrm == "X++" or prgrm == "++X":
        x += 1
    else:
        x-= 1
print(x)
