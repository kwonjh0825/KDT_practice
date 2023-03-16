import sys
from collections import Counter

input = sys.stdin.readline

# pr01. 2441: 별 찍기-4
n = int(input())
for i in range(n):
    print(' '*i + '*'*(n-i))

# pr02. 2592: 대표값
li = [int(input()) for _ in range(10)]
cnt = Counter(li)
sorted_cnt = sorted(cnt.items(), key=lambda x: -x[1])

print(sum(li)//10, sorted_cnt[0][0])

# pr03. 10798: 세로 읽기
li = []
for i in range(5):
    li.append(list(input().strip()))
    if len(li[i]) < 15:
        li[i].extend([0] * (15 - len(li[i])))

for i in range(15):
    for j in range(5):
        if li[j][i] == 0:
            continue
        else:
            print(li[j][i], end='')

# pr04. 9455: 박스
T = int(input())

for _ in range(T):
    box = []
    ans = 0
    m, n = map(int, input().split())
    for _ in range(m):
        box.append(list(map(int, input().split())))
    
    for i in range(n):
        cnt = 0
        for j in range(m-1, -1, -1):
            if box[j][i]:
                ans += cnt
            else:
                cnt += 1
    
    print(ans)


# pr05. 1652: 누울 자리를 찾아라
N = int(input())
room = [list(input().strip()) for _ in range(N)]
rotated_room = [['']*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        rotated_room[i][j] = room[j][N-i-1]
ver_cnt = 0
hor_cnt = 0

for r, rr in zip(room, rotated_room):
    len_r = 0
    len_rr = 0
    for i in range(N):
        if r[i] == '.':
            len_r += 1
        elif r[i] == 'X':
            if len_r > 1:
                hor_cnt += 1
                len_r = 0
            else:
                len_r = 0
        
        if rr[i] == '.':
            len_rr += 1
        elif rr[i] == 'X':
            if len_rr > 1:
                ver_cnt += 1
                len_rr = 0
            else:
                len_rr = 0
    
    if len_r > 1:
        hor_cnt += 1                
    if len_rr > 1:
        ver_cnt += 1

print(hor_cnt, ver_cnt)


