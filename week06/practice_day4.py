import sys

input = sys.stdin.readline

# pr01. 1547: 공
M = int(input())
ball = {1: 1, 2: 0, 3: 0}

for _ in range(M):
    x, y = map(int, input().split())
    if ball[x] or ball[y]:
        ball[x], ball[y] = ball[y], ball[x]

print(sorted(ball.items(), key=lambda x: -x[1])[0][0])

# pr02. 5576: 콘테스트
w_score = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
k_score = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
print(w_score, k_score)

# pr03. 2846. 오르막길
N = int(input())
li = list(map(int, input().split()))
up_cnt = 0
up_start = 0
ans = [0]

for i in range(1, len(li)):
    if li[i-1] < li[i] and up_cnt == 1:
        pass
    elif li[i-1] < li[i] and up_cnt == 0:
        up_start = li[i-1]
        up_cnt = 1
    elif not li[i-1] < li[i] and up_cnt == 1:
        ans.append(li[i-1] - up_start)
        up_start = 0
        up_cnt = 0
    else:
        up_cnt = 0
        up_start = 0
if up_cnt:
    ans.append(li[-1] - up_start)
print(max(ans))

# pr04. 1251: 단어 나누기
string = input().strip()
ans = []
for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        ans.append(a+b+c)
print(sorted(ans)[0])