# pr01. 10101: 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b and b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

# pr02. 2720: 세탁소 사장 동혁
T = int(input())
for _ in range(T):
    cnt = []
    dollar = int(input())
    cnt.append(dollar//25)
    dollar = dollar % 25

    cnt.append(dollar//10)
    dollar = dollar % 10

    cnt.append(dollar//5)
    dollar = dollar % 5

    cnt.append(dollar)
    print(*cnt)

# pr03. 1453: 피시방 알바
input()
li = list(map(int, input().split()))
now = []
cnt = 0
for l in li:
    if l not in now:
        now.append(l)
    else:
        cnt += 1
print(cnt)

# pr04. 10773: 제로
import sys
input = sys.stdin.readline

k = int(input())
li = []
for _ in range(k):
    n = int(input())
    if n:
        li.append(n)
    else:
        li.pop()
print(sum(li))

# pr05. 2161: 카드1
from collections import deque

n = int(input())
li = deque(x for x in range(1, n+1))
for _ in range(n):
    print(li.popleft())
    if li:
        li.append(li.popleft())

# pr06. 9012: 괄호
T = int(input())
for _ in range(T):
    string = input()
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')