import sys

t = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

sensors = [int(i) for i in sys.stdin.readline().strip().split()]

sensors.sort()

sub = []
for i in range(1, t):
    sub.append(sensors[i] - sensors[i - 1])
sub.sort()
for i in range(k - 1):
    if len(sub) == 0:
        break
    sub.pop()
print(sum(sub))