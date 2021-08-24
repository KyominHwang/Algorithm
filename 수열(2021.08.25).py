import sys

t = int(sys.stdin.readline().strip())

arr = [int(i) for i in sys.stdin.readline().strip().split()]

cnt = 1
maxval = 1
for i in range(1, t):
    if arr[i - 1] >= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if maxval < cnt:
        maxval = cnt
cnt = 1

for i in range(1, t):
    if arr[i - 1] <= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if maxval < cnt:
        maxval = cnt
print(maxval)