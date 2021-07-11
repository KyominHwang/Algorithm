import sys

cnt = 1
while True:
    case = [int(i) for i in sys.stdin.readline().strip().split()]
    if case[0] == case[1] == case[2] == 0:
        break
    t = case[2] // case[1]
    ans = t * case[0] + min(case[0], case[2] - t * case[1])
    print(f"Case {cnt}: {ans}")
    cnt += 1