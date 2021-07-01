import sys
tmp = sys.stdin.readline().split()
n,m,k = int(tmp[0]), int(tmp[1]), int(tmp[2])
arr = [int(i) for i in sys.stdin.readline().split()]
arr_sorted = sorted(arr)

global_cnt = 0
local_cnt = 0
ans = 0
# 가장 큰 값을 가짐
curval = arr_sorted[-1]
maxval = curval
while True:
    if global_cnt == m:
        break
    ans += curval
    local_cnt += 1
    global_cnt += 1
    if maxval > curval:
        local_cnt = 0
        curval = maxval
    elif local_cnt == k:
        local_cnt = 0
        curval = arr_sorted[-2]
print(ans)