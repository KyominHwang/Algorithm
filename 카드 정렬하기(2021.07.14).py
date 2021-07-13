import sys
import heapq
t = int(sys.stdin.readline().strip())
que = []
for i in range(t):
    heapq.heappush(que, (int(sys.stdin.readline().strip())))
if len(que) > 1:
    ans = 0
    while len(que) > 1:
        prev = heapq.heappop(que)
        cur = heapq.heappop(que)
        ans += prev + cur
        heapq.heappush(que, prev + cur)
    print(ans)
else:
    print(0)