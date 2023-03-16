# pr01. 17608: 막대기
N = int(input())
li = [int(input()) for _ in range(N)]
max_height = 0
cnt = 0
for l in reversed(li):
    if l > max_height:
        cnt += 1
        max_height = l
print(cnt)

# pr02. 7568: 덩치
n = int(input())
li = []
cnt_list = []
for i in range(n):
    li.append(list(map(int, input().split())))
for i in li:
    cnt = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    cnt_list.append(cnt)

print(*cnt_list)

# pr03. 1063: 킹
a, b, n = input().split()
n = int(n)

direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, 1), 'T': (0, -1), 'RT': (1, -1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (-1, 1)}
king_x, king_y = ord(a[0]) - 65, 8 - int(a[1])
stone_x, stone_y = ord(b[0]) - 65, 8 - int(b[1])

for _ in range(n):
    t = input()
    king_nx, king_ny = king_x + direction[t][0], king_y + direction[t][1]
    if 0 <= king_nx < 8 and 0 <= king_ny < 8:
        if (king_nx, king_ny) == (stone_x, stone_y):
            stone_nx, stone_ny = stone_x + direction[t][0], stone_y + direction[t][1]
            if 0 <= stone_nx < 8 and 0 <= stone_ny < 8:
                stone_x, stone_y = stone_nx, stone_ny
                king_x, king_y = king_nx, king_ny
        else:
            king_x, king_y = king_nx, king_ny
print(f'{chr(king_x+65)}{8 - king_y}', f'{chr(stone_x+65)}{8-stone_y}', sep='\n')
