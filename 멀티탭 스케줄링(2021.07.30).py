import sys
import collections
import heapq
n, k = map(int, sys.stdin.readline().strip().split())

order = [int(i) for i in sys.stdin.readline().strip().split()]

queue = collections.deque()

ans = 0
for i in range(len(order)):
    if order[i] in queue:
        continue
    elif len(queue) < n:
        queue.append(order[i])
    else:
        t = []
        a =set()
        for j in range(i + 1, len(order)):
            if order[j] in queue and order[j] not in a:
                heapq.heappush(t,[-1 * j, order[j]])
                a.add(order[j])
        if len(set(queue) - a) != 0:
            queue.remove(list(set(queue) - a)[0])
            queue.append(order[i])
            ans += 1
        else:
            queue.remove(heapq.heappop(t)[1])
            queue.append(order[i])
            ans += 1

print(ans)