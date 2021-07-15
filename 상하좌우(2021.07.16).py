import sys

n = int(sys.stdin.readline().strip())

command = [i for i in sys.stdin.readline().strip().split()]
x, y = 1, 1
for c in command:
    if c == "R":
        if 0 < y + 1 <= n:
            y += 1
    elif c == "U":
        if 0 < x - 1 <= n:
            x -= 1
    elif c == "D":
        if 0 < x + 1 <= n:
            x += 1
    else:
        if 0 < y - 1 <= n:
            y -= 1
print(x,y)