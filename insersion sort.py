n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
def insertionSort1(n, arr):
    # Write your code here
    x= arr[n-1]
    ind = n-1
    for i in range(n):
        if arr[ind] < arr[ind-1]:
            
            arr[ind] = arr[ind-1]
        
            for i in arr:
                print (i,end=' ')
            print("")
            arr[ind-1]= x
            ind-=1
            if ind <=0:
                break
    for i in arr:
        print (i,end=' ')
    print("")
        
insertionSort1(n, arr)
