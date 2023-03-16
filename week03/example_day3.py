import sys

# ex01
sys.stdin = open('input.txt', 'r')
li = list(map(int, input().split()))

for l in li:
    print(l, end=' ')
sys.stdin.close()

# ex02
sys.stdin = open('input.txt', 'r')
li = list(input().split())
for l in li:
    print(l, end=' ')
    print()
sys.stdin.close()

# ex03
T = int(input())

for _ in range(T):
    line = int(input())
    for _ in range(line):
        print(int(input()))

# ex04
T = int(input())

for _ in range(T):
    n = int(input())
    for i in range(1, n + 1):
        print(i, i)

# ex05
T = int(input())

for _ in range(T):
    n = int(input())
    with open('input.txt', 'r', encoding='UTF8') as f:
        for i in range(n):
            print(f.readline().strip())
    
# ex06
T = int(input())
with open('input.txt', 'r', encoding='UTF8') as f:
    for _ in range(T):
        n = int(input())
        for _ in range(n):
            li = list(map(int, f.readline().split()))
            for l in li:
                print(l, end=' ')
            print()
    
# ex07
T, line = map(int, input().split())
for t in range(1, T + 1):  
    for l in range(line):
        print(input())

# ex08
T, line = map(int, input().split())
for t in range(1, T + 1):  
    for l in range(line):
        print(input())

# ex09
T, line = map(int, input().split())
for _ in range(T):
    for l in range(line):
        print(input())