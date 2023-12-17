m,n=map(int, input("Enter m n: ").split())
arr=[]
for i in range(m):
    row=[]
    for j in range(n):
        value = int(input("Enter {},{}: ".format(i,j)))
        row.append(value)
    arr.append(row)
print("printing in snake")
for i in range(m):
    if i%2==0:
        for j in range(n):
            print(arr[i][j])
    else:
        for j in range(n-1,-1,-1):
            #print("j: ",j)
            print(arr[i][j])
