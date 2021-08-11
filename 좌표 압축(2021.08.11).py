import sys

n = int(sys.stdin.readline().strip())

nums = [int(i) for i in sys.stdin.readline().strip().split()]

k = list(set(nums))
k.sort()
dict = {}
cnt = 0
for i in range(len(k)):
    if k[i] not in dict:
        dict[k[i]] = cnt
        cnt += 1
for i in nums:
    print(dict[i], end=" ")