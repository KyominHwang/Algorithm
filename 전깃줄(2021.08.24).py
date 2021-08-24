import sys

t = int(sys.stdin.readline().strip())
dp = [0 for i in range(t + 1)]
arr = [[0,0]]
for i in range(t):
    arr.append([int(i) for i in sys.stdin.readline().strip().split()])
arr.sort()
print(arr)
for i in range(1, t + 1):
    dp[i] = 1
    for j in range(1, i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(t - max(dp))