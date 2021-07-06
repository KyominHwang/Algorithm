import sys
t = int(sys.stdin.readline())
for test in range(t):
    n = int(sys.stdin.readline())
    scores = []
    for i in range(n):
        scores.append(list(map(int, sys.stdin.readline().split())))
    scores.sort()
    minval = scores[0][1]
    cnt = 1
    for i in range(1, len(scores)):
        if minval > scores[i][1]:
            cnt += 1
            minval = min(minval, scores[i][1])
    print(cnt)