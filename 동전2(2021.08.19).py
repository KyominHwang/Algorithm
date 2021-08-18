import sys
n, k = map(int, sys.stdin.readline().strip().split())
dp = [0 for i in range(k + 1)]
coins = []
for i in range(n):
    t = int(sys.stdin.readline().strip())
    if t < len(dp):
        dp[t] = 1
        coins.append(t)
for i in range(1, len(dp)):
    flag = False
    for j in range(len(coins)):
        if i - coins[j] > 0 and dp[i - coins[j]] != -1:
            if dp[i] == 0:
                dp[i] = 1 + dp[i - coins[j]]
                flag = True
            else:
                dp[i] = min(1 + dp[i - coins[j]], dp[i])
                flag = True
    if flag == False and dp[i] == 0:
        dp[i] = -1
print(dp[-1])