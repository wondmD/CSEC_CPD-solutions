piles = [9,8,7,6,5,1,2,3,4]
piles.sort(reverse=True)
p = 1
my_coin = 0
print (piles)
for i in range(len(piles)):
    if p == 2 :
        print (piles[i])
        my_coin += piles[i]
        p+=1
    elif p == 3:
        p=1
    else :
        p+=1
print (my_coin)