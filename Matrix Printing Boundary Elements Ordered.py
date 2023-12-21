m, n = map(int, input("Enter m n: ").split())
arr=[]
for i in range(m):
    row=[]
    for j in range(n):
        value = int(input("Enter ({},{}): ".format(i,j)))
        row.append(value)
    arr.append(row)

print("Priting array elements in Order")

result=[]
# Top boundary
for j in range(0,n):
    result.append(arr[0][j])
# Right boundary
for i in range(m):
    if i>0 and i<m-1:
        result.append(arr[i][n-1])
# Bottom boundary
for j in range(n-1,-1,-1):
    result.append(arr[m-1][j])
# Left boundary
for i in range(m-1,-1,-1):
    if i>0 and i<n-1:
        result.append(arr[i][0])
print("Result: ",result)
