import sys

size = [int(i) for i in sys.stdin.readline().strip().split()]

tmp = [int(i) for i in sys.stdin.readline().strip().split()]
x = tmp[0]
y = tmp[1]
dir = tmp[2]

map = []

for i in range(size[0]):
    map.append([int(i) for i in sys.stdin.readline().strip().split()])

order = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
while True:
    flag = False
    map[x][y] = -1
    for i in range(4):
        dir = (dir + 4 - 1) % 4
        if map[x + order[dir][0]][y + order[dir][1]] == 0:
            x += order[dir][0]
            y += order[dir][1]
            flag = True
            break
    if flag:
       continue
    else:
        if map[x - order[dir][0]][y - order[dir][1]] == 1:
            break
        x -= order[dir][0]
        y -= order[dir][1]

ans = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == -1:
            ans += 1
print(ans)