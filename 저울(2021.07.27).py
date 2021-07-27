import sys

t = int(sys.stdin.readline().strip())

nums = [int(i) for i in sys.stdin.readline().strip().split()]
nums.sort()

ans = 0
for i in range(len(nums)):
    if ans + 1 < nums[i]:
        break
    ans += nums[i]
print(ans + 1)