l = []
try :
    n = int(input())
except :
    print ("error")
for i in range(1,n+1):
    if i%5 == 0 and i%3 ==0:
        l.append("FizzBuzz")
    elif i%5 == 0:
        l.append("Buzz")
    elif i%3 == 0:
        l.append("Fizz")
    else :
        l.append(str(i))
print (l)