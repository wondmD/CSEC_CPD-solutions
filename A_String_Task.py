v = 'aeiouy'
s = input().lower()
out = ""
for i in s:
    if not i in v:
        out+="."
        out+=i
print (out)