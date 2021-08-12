import sys
import heapq

n = int(sys.stdin.readline().strip())

nums = []
for i in range(n):
    tmp = [int(i) for i in sys.stdin.readline().strip().split()]
    for j in range(n):
        heapq.heappush(nums, tmp[j])
    while len(nums) > n:
        heapq.heappop(nums)
print(nums[0])