import sys
sys.setrecursionlimit(10000)

# pr01. 10769: 행복한지 슬픈지
string = input().split(':')

cnt_happy = 0
cnt_sad = 0

for s in string:
    if '-(' in s:
        cnt_sad += 1
    elif '-)' in s:
        cnt_happy += 1

if not cnt_happy and not cnt_sad:
    print('none')
elif cnt_happy > cnt_sad:
    print('happy')
elif cnt_happy < cnt_sad:
    print('sad')
else:
    print('unsure')

# pr02. 2455: 지능형 기차
max_client = 0
now = 0
for _ in range(4):
    a, b = map(int, input().split())
    now -= a
    now += b
    max_client = max(max_client, now)
print(max_client)

# pr03. 2606: 바이러스
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    stack = [s]
    visited[s] = True
    while stack:
        current = stack.pop()

        for adj in graph[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)

print(len([x for x in visited if x]) - 1)

# pr04. 4963: 섬의 개수
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    
    ans = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [[False] * w for _ in range(h)]
    
    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] and not visited[nx][ny]:
                    dfs(nx, ny)
    
    for x in range(h):
        for y in range(w):
            if graph[x][y] and not visited[x][y]:
                dfs(x, y)
                ans += 1
    print(ans)