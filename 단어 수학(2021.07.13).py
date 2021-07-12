import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    tmp = sys.stdin.readline().strip()[::-1]
    num_list.append(tmp)

num_cnt = dict()
for i in range(len(num_list)):
    pow = 10
    for j in range(len(num_list[i])):
        if num_list[i][j] not in num_cnt.keys():
            num_cnt[num_list[i][j]] = pow ** j
        else:
            num_cnt[num_list[i][j]] += pow ** j

sorted_list = []
for k, v in num_cnt.items():
    sorted_list.append([v, k])
sorted_list.sort(reverse=True)

num = 9
num_map = dict()
for i in range(len(sorted_list)):
    num_map[sorted_list[i][1]] = num
    num -= 1

ans = 0
for i in range(n):
    tmp = ""
    for j in range(len(num_list[i])):
        tmp += str(num_map[num_list[i][j]])
    ans += int(tmp[::-1])
print(ans)