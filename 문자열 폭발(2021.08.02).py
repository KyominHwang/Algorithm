import sys

data = [i for i in sys.stdin.readline().strip()]
boom = sys.stdin.readline().strip()

ans = []
for i in range(len(data)):
    ans.append(data[i])
    while len(ans) > 0 and ans[-1] == boom[-1] and "".join(ans[len(ans) - len(boom):]) == boom:
        del ans[len(ans) - len(boom):]
if len(ans) == 0:
    print("FRULA")
else:
    print("".join(ans))