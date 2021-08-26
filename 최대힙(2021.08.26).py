import sys
import heapq

t = int(sys.stdin.readline().strip())

arr = []

for i in range(t):
    a = int(sys.stdin.readline().strip())
    if a != 0:
        heapq.heappush(arr, -1 * a)
    else:
        if len(arr) != 0:
            val = heapq.heappop(arr)
        else:
            val = 0
        print(val * -1)