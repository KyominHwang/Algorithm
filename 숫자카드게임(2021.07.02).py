import sys

tmp = sys.stdin.readline().split()
n, m = int(tmp[0]), int(tmp[1])

minvals = []
for i in range(n):
    tmp = [int(i) for i in sys.stdin.readline().split()]
    minvals.append(min(tmp))
print(max(minvals))