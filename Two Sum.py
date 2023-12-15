n = int(input("Enter n: "))
arr = list(map(int, input().split()))
k = int(input("Enter k: "))
l = 0
r = n-1
res = 'no'
while r>=0 and l<=n-1:
    if arr[l]+arr[r]==k:
        res = 'yes'
        break
    elif arr[l]+arr[r]>k:
        r=r-1
    else:
        l=l+1
print(res)
    


        
    
