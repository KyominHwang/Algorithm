import sys
from collections import deque
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline().strip())

network = []
visited = [[False] * n for i in range(n)]

for i in range(n):
    network.append([1 if i == "R" else (2 if i == "G" else 3) for i in sys.stdin.readline().strip()])


def dfs(i, j, val):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append([i, j])
    while len(queue) > 0:
        pos = queue.popleft()
        visited[pos[0]][pos[1]] = True
        for k in range(4):
            x = pos[0] + dir[k][0]
            y = pos[1] + dir[k][1]
            if not (0 <= x < n and 0 <= y < n):
                continue
            if not visited[x][y] and network[x][y] == val:
                dfs(x, y, val)


ansNormal = 0
ansAbnormal = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, network[i][j])
            ansNormal += 1

for i in range(n):
    for j in range(n):
        if network[i][j] == 1 or network[i][j] == 2:
            network[i][j] = 1
        else:
            network[i][j] = 2

visited = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, network[i][j])
            ansAbnormal += 1

print(ansNormal, ansAbnormal)
