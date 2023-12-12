n = int(input("Enter N: "))
arr = list(map(int, input().split()))
result = n+1
for i in range(0, len(arr)):
    value = abs(arr[i])-1
    if value<n:
        arr[value] = abs(arr[value])*(-1)
for i in range(0,len(arr)):
    if arr[i]>0:
        result = i+1
        break
print(result)
print('arr: ', arr)
