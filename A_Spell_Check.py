for i in range(int(input())):
    n = int(input())
    s = input()
    if n != 5:
        print ("NO")
        continue
    elif sorted(s) == sorted("Timur"):
        print ("YES")
    else :
        print ("NO")
        