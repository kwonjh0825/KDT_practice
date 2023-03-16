import sys

input = sys.stdin.readline

# pr01. 1225: 이상한 곱셈
n, m = input().split()
n = list(map(int, n))
m = list(map(int, m))
print(sum(n)*sum(m))

# pr02. 2438: 별 찍기-1
for i in range(1, int(input())+1):
    print('*'*i)

# pr03. 2739: 구구단
n = int(input())
for i in range(1, 10):
    print(f'{n} * {i} = {n*i}')

# pr04. 2953: 나는 요리사다
li = [list(map(int, input().split())) for _ in range(5)]
ans = 0
idx = 0
for i, l in enumerate(li):
    if sum(l) > ans:
        idx = i+1
        ans = sum(l)
print(idx, ans)

# pr05. 2669: 직사각형 네개의 합집합의 넓이
ground = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            ground[x][y] = 1
for g in ground:
    ans += g.count(1)
print(ans)