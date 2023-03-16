# pr01. 9085: 더하기
T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(list(map(int, input().split()))))

# pr02. 10824: 네 수
a, b, c, d = input().split()
print(int(a+b)+int(c+d))

# pr03. 3009: 네 번째 점
rect = []
x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    rect.append([a, b])

for i in x:
    for j in y:
        if [i, j] not in rect:
            print(i, j)
            break

# pr04. 10952: A+B-5
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# pr05. 1110: 더하기 사이클
N = input()
if len(N) < 2:
    N = '0' + N
new_num = N[-1] + str(sum(list(map(int, N))))[-1]
cnt = 1
while new_num != N:
    new_num = new_num[-1] + str(sum(list(map(int, new_num))))[-1]
    cnt += 1
print(cnt)
