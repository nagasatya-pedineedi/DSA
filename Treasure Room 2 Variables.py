n, w = map(int, input().split())
arr = list(map(int, input().split()))

block_indexes = {}
flag=False
for i, block in enumerate(arr):
    diff = w - block
    if diff in block_indexes:
        flag=True
        print(block_indexes[diff] + 1, i + 1)
        break
    else:
        block_indexes[block] = i
if flag==False:
    print(-1)
