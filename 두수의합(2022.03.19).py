import sys
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
target = int(sys.stdin.readline())
ans = 0
p1, p2 = 0, len(arr) - 1
while p1 < p2:
    if arr[p1] + arr[p2] == target:
        ans += 1
        p1 += 1
        p2 -= 1
    elif arr[p1] + arr[p2] > target:
        p2 -= 1
    else:
        p1 += 1
print(ans)