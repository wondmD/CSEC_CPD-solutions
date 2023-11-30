names = ["Mary","John","Emma"]
heights = [180,165,170]

d = {}
n = len(names)
for i in range(n):
    d[heights[i]] = names[i]
heights.sort(reverse=Truetst)
for i in range(n):
    names[i] = d[heights[i]]
print (names)
        