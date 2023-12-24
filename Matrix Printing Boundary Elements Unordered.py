m,n = map(int, input("Enter m n: ").split())
arr=[]
for i in range(m):
    row = []
    for j in range(n):
        value = int(input("Enter ({},{}): ".format(i,j)))
        row.append(value)
    arr.append(row)
print("## Array Entered ##")
print(arr)

result=[]
for i in range(m):
    for j in range(n):
        if i==0 or i==m-1 or j==0 or j==n-1:
           result.append(arr[i][j])
print("Result: ", result)
