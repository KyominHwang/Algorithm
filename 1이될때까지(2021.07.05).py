import sys

tmp = sys.stdin.readline().split()
n , k = int(tmp[0]), int(tmp[1])
cnt = 0
while n != 1:
    if n % k == 0:
        n = n // k
    else:
        n = n - 1
    cnt += 1
print(cnt)