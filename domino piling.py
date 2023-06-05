x,y = map(int, input().split())
total_area = x*y
if total_area%2 == 0 :
    print(total_area//2)
else:
    print ((total_area-1)//2)