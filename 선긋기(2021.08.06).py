import sys

t = int(sys.stdin.readline().strip())
lines =[]
for i in range(t):
    lines.append([int(i) for i in sys.stdin.readline().strip().split()])
lines.sort(key=lambda x: x[0])
ans = 0
start = lines[0][0]
end = lines[0][1]
for i in range(1, t):
    if start <= lines[i][0] <= end and lines[i][1] >= end:
        end = lines[i][1]
    elif start <= lines[i][0] <= end and lines[i][1] < end:
        continue
    else:
        ans += end - start
        start = lines[i][0]
        end = lines[i][1]
print(ans + (end - start))