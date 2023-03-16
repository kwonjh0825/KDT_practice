# pr01 : 신문 헤드라인
print(input().upper())

# pr02 : n줄 덧셈
n = int(input())
print(int((n * (n+1)) / 2))


# pr03 : 1대1 가위바위보
a, b = map(int, input().split())
if a < 3:
    if b == (a + 1):
        print('B')
    else:
        print('A')
else:
    if b == 1:
        print('B')
    else:
        print('A')

# pr03_v2
a, b = map(int, input().split())
result = [0, 1, 2, 3, 1]

if result[b] == result[a+1]:
    print('B')
else:
    print('A')

# pr04 : 대각선 출력하기
for i in range(5):
    print(('+'* i) + '#' + '+'*(4-i))

# pr05 : 자릿수 더하기
n = input()
ans = 0
for i in n:
    sum += int(i)
print(ans)

# pr05_v2
n = int(input())
ans = 0
while n > 0:
    ans += n % 10
    n = n // 10
print(ans)

# pr06 : 더블더블
n = int(input())
for i in range(n+1):
    print(2**i, end=' ')