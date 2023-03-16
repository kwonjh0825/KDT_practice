# ex01
a, b = map(int, input().split())
print(a+b)

# ex02
a = int(input())
b = int(input())
print(a+b)

# ex03 
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a+b)

# ex04
T = int(input())
for _ in range(T):
    a, b = map(int, input().split(','))
    print(a+b)

# ex05
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a+b}')

# ex06
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a} + {b} = {a+b}')