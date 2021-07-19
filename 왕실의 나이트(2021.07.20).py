import sys

pos = sys.stdin.readline().strip()

x, y = int(ord(pos[0])) - int(ord('a')), int(pos[1]) - 1

vari = [[-2,-1],[1,-2],[2,1],[-1,2],[2,-1],[1,2],[-2,1],[-1,-2]]

ans = 0
for i in range(8):
    i_x, i_y = vari[i][0], vari[i][1]
    if 0 <= i_x + x < 8 and 0<= i_y + y < 8:
        ans += 1
print(ans)