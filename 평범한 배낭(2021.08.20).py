import sys

n, k = map(int, sys.stdin.readline().strip().split())

dp = [[0] * (k + 1) for i in range(n + 1)]

vals = [[0,0]]

for i in range(n):
    vals.append([int(i) for i in sys.stdin.readline().strip().split()])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= vals[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vals[i][0]] + vals[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])