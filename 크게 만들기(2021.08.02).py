import sys

n, k = map(int, sys.stdin.readline().strip().split())

num = [i for i in sys.stdin.readline().strip()]

ans = []
i = 0
while k > 0 and i < len(num):
    if len(ans) == 0:
        ans.append(num[i])
        i += 1
    else:
        while len(ans) > 0 and ans[-1] < num[i] and k > 0:
            del ans[-1]
            k -= 1
        ans.append(num[i])
        i += 1
if i < len(num):
    for p in range(i, len(num)):
        ans.append(num[p])
if k > 0:
    ans = ans[:-k]
print("".join(ans))