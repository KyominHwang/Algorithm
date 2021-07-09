import sys
t = int(sys.stdin.readline())
path = [int(i) for i in sys.stdin.readline().split()]
money = [[int(k), int(i)] for i, k in enumerate(sys.stdin.readline().split())]

money.sort()
ans = 0

for i in range(1, len(path)):
    path[len(path) - i - 1] = path[len(path) - i - 1] + path[len(path) - i]
complete = len(money) - 1
path.append(0)
for i in range(len(money)):
    tmp = money[i][1]
    if tmp == len(money) - 1:
        continue
    elif tmp > complete:
        continue
    ans += money[i][0] * (path[tmp] - path[complete])
    complete = tmp
print(ans)