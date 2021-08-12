import sys
import heapq
n = int(sys.stdin.readline().strip())

data = []

for i in range(n):
    t = [int(i) for i in sys.stdin.readline().strip().split()]
    data.append([int(t[0]), int(t[1])])
data.sort(key=lambda x : x[1])
nums = []
for i in range(len(data)):
    heapq.heappush(nums, data[i][0])
    if len(nums) > data[i][1]:
        heapq.heappop(nums)

print(sum(nums))