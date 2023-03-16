import sys
from itertools import combinations

input = sys.stdin.readline

# pr01. 2525: 오븐 시계
a, b = map(int, input().split())
c = int(input())

b += c
if b >= 60:
    a += (b // 60)
    if a >= 24:
        a -= 24
    b = b % 60
print(a, b)


# pr02. 2798: 블랙잭
n, m = map(int, input().split())
li = list(map(int, input().split()))

combs = list(combinations(li, 3))
ans = 0
for c in combs:
    if sum(c) > m:
        continue
    elif sum(c) > ans:
        ans = sum(c)
print(ans)

# pr03. 9076: 점수 집계
T = int(input())
for _ in range(T):
    li = sorted(list(map(int, input().split())))
    if li[-2] - li[1] > 3:
        print('KIN')
    else:
        print(sum(li[1:4]))

# pr04. 1526: 가장 큰 금민수
for i in range(int(input()), 1, -1):
    for s in str(i):
        if s in '01235689':
            break
    else:
        print(i)
        break

# pr05. 1436: 영화감독 숌
n = int(input())
li = []
i = 1
while len(li) < 10001:
    if '666' in str(i):
        li.append(i)
    i += 1
print(li[n-1])