import sys
n, m = [int(i) for i in sys.stdin.readline().strip().split()]

dp = [1,n]

for i in range(2, m + 1):
    dp.append(dp[-1] * (n - (i - 1)) // i)
print(dp[-1])