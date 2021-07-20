import sys

size = [int(i) for i in sys.stdin.readline().strip().split()]

tmp = [int(i) for i in sys.stdin.readline().strip().split()]
x = tmp[0]
y = tmp[1]
dir = tmp[2]

map = []

for i in range(size[0]):
    map.append([int(i) for i in sys.stdin.readline().strip().split()])

order = {0:[0,-1],1:[1,0],2:[0,1],3:[-1,0]}
ans = 0
map[x][y] = -1
while True:
    flag = False
    for i in range(4):
        dir = (dir + 4 - 1) % 4
        if map[x + order[dir][0]][y + order[dir][1]] == 0:
            map[x + order[dir][0]][y + order[dir][1]] = -1
            x += order[dir][0]
            y += order[dir][1]
            flag = True
            break
    if flag:
       ans += 1
    else:
        if map[x + order[(dir + 4 - 2) % 4][0]][y + order[(dir + 4 - 2) % 4][1]] == 1:
            break
        ans += 1
        x += order[(dir + 4 - 2) % 4][0]
        y += order[(dir + 4 - 2) % 4][1]
print(ans)