import sys
t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    dp = [[int(i) for i in sys.stdin.readline().strip().split()]]
    dp.append([int(i) for i in sys.stdin.readline().strip().split()])
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
    print(max(dp[0][-1], dp[1][-1]))