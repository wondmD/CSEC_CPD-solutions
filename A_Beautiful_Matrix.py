l = [0] *5
x = 0
y=0
for i in range(5):
    l[i] = list(map(int, input().split()))
    if 1 in l[i] :
        x = i
        y = l[i].index(1)
h_move = abs(2-x)
v_move = abs(2-y)
print(h_move + v_move)