import sys

exp = sys.stdin.readline().strip()

if len(exp) % 2 == 1:
    print("Keine Loesung")
else:
    stack = []
    ans = ""
    flag = True
    for i in range(0,len(exp), 2):
        if len(stack) == 0:
            sc = exp[i]
        if exp[i] == sc and exp[i + 1] == sc:
            stack.append("[")
            ans += "["
        elif exp[i] != sc and exp[i + 1] != sc:
            if len(stack) != 0 and stack[-1] == "[":
                ans += "]"
                stack.pop()
            else:
                print("Keine Loesung")
                flag=False
                break
        else:
            print("Keine Loesung")
            flag=False
            break
    if flag and len(stack) == 0:
        print(ans)
    if flag and len(stack) != 0:
        print("Keine Loesung")