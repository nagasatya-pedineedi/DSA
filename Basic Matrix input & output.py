m, n = map(int, input("Enter m,n: ").split())
#print(m,n)
arr = []
for i in range(m):
    row = []
    for j in range(n):
        value = int(input("Enter {},{} value: ".format(i,j)))
        row.append(value)
    arr.append(row)
print("Printing")
#for i in arr:
#    print(i)
for i in range(m):
    for j in range(n):
        print("value in arr[{}][{}]: {}".format(i,j, arr[i][j]))
