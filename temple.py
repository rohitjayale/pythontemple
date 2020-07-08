m=int(input())
for i in range(m):
    l=int(input())
    arr=list(map(int,input().split()))
    total=0
    arr.sort()
    while l>3:
        total+=min((2*arr[0]+arr[l-1]+arr[l-2],(arr[0]+2*arr[1]+arr[l-1])))
        l-=2
    if (l==3):
        total+=arr[0]+arr[1]+arr[2]
    elif(l==2):
        total+=arr[1]
    else:
        total+=arr[0]
    print(total)
    
    
 
