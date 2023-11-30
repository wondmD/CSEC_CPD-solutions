n = int(input())
s = input()[:n]
if s.count("A") > s.count("D"):
    print ("Anton")
elif s.count("A") < s.count("D"):
    print ("Danik")
else:
    print ("Friendship")