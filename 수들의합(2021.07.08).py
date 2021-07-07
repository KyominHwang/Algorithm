import sys

n = int(sys.stdin.readline())
ans = 0
target = n
data = []
for i in range(1,n + 1):
    if target - i >= 0:
        ans += 1
        target -= i
        data.append(i)
    else:
        break
print(len(data))