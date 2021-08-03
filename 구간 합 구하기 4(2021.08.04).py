import sys

n, t = map(int, sys.stdin.readline().strip().split())

nums = [int(i) for i in sys.stdin.readline().strip().split()]

for i in range(1, len(nums)):
    nums[i] = nums[i] + nums[i - 1]
nums.insert(0,0)
for i in range(t):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(nums[b] - nums[a - 1])