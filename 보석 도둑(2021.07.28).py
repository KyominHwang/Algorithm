import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
product = []
for i in range(n):
    heapq.heappush(product, [int(i) for i in sys.stdin.readline().strip().split()])

bag = []
for i in range(m):
    bag.append(int(sys.stdin.readline().strip()))
bag.sort()

ans = 0
tmp = []
for i in range(len(bag)):
    while product and bag[i] >= product[0][0]:
        heapq.heappush(tmp, -1 * product[0][1])
        heapq.heappop(product)
    if tmp:
        ans += heapq.heappop(tmp)
    elif not product:
        break

print(-1 * ans)