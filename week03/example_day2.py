import sys

# ex01
print(int(input('정수를 출력하세요 > ')))

# ex02
li = list(input().split())
for l in li:
    print(l, end=' ')
print()

# ex03
T = int(input('테스트 케이스마다 입력 값을 그대로 출력하세요 > '))
for t in range(1, T+1):
    print(t)

# ex04
li = list(map(int, input().split()))
for n in li:
    print(n, end=' ')
print()

# ex05
a, b = map(int, input().split())
print(a, b)

# ex06
li = list(input().split())
for l in li:
    print(l, end=' ')
print()

# ex07
T = int(input())
for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().split())
    print(a, b, c)

# ex08
T = int(sys.stdin.readline())
for _ in range(T):
    li = list(map(int, sys.stdin.readline().split()))
    for l in li:
        print(l, end=' ')
    print()