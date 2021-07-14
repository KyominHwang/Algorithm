import sys

nums_minus = []
nums_positive = []
t = int(sys.stdin.readline().strip())
ans = 0
for i in range(t):
    num = int(sys.stdin.readline().strip())
    if num == 1:
        ans += 1
    elif num > 0:
        nums_positive.append(num)
    else:
        nums_minus.append(num)
nums_positive.sort(reverse=True)
nums_minus.sort()
for i in range(1, len(nums_minus),2):
    ans += nums_minus[i] * nums_minus[i - 1]
if len(nums_minus) % 2 != 0:
    ans += nums_minus[-1]
for i in range(1,len(nums_positive),2):
    ans += nums_positive[i] * nums_positive[i - 1]
if len(nums_positive) %2 != 0:
    ans += nums_positive[-1]
print(ans)