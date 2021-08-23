import sys

t = int(sys.stdin.readline().strip())
dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(dp[n])