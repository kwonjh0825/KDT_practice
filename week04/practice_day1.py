# # pr01. 10039: 평균 점수
# scores = []
# for _ in range(5):
#     score = int(input())
#     scores.append(scores) if score > 40 else scores.append(40)
# print(int(sum(scores)/len(scores)))

# # pr02. 10871: x보다 작은 수
# n, x = map(int, input().split())
# li = list(map(int, input().split()))
# for num in li:
#     if num < x:
#         print(num, end=' ')

# # pr03. 2480: 주사위 세개
# num_li = sorted(map(int, input().split()))
# t = len(set(num_li))
# if t == 1:
#     print(10000+(num_li[0]*1000))
# elif t == 2:
#     print(1000+(num_li[1]*100))
# else:
#     print(100*(max(num_li)))

# # pr04. 10886: 0 = not cute / 1 = cute
# N = int(input())
# survey = [int(input()) for _ in range(N)]
# ans = 0 if survey.count(1) > survey.count(0) else 1 # 0: cute, 1: not cute
# print('Junhee is ' + (ans * 'not ') + 'cute!')

# pr05. 2506: 점수 계산
N = int(input())
score = list(map(int, input().split()))
ans, cnt = 0, 0
# for s in score:
#     if s:
#         cnt += 1
#         ans += cnt
#     else:
#         cnt = 0

while len(score) > 0:
    s = score.pop()
    if s:
        cnt += 1
        ans += cnt
    else:
        cnt = 0

print(ans)


