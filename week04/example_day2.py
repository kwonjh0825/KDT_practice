# ex01. 10818: 최대, 최소
n = int(input())
a = list(map(int, input().split(" ")))

print(min(a), max(a))

# ex02. 11720: 숫자의 합
n = int(input())
a = list(map(int, input()))
print(sum(a))

# ex03. 2750: 수 정렬하기
N = int(input())
li = [int(input()) for _ in range(N)]
print(*sorted(li), sep='\n')

# ex04. 2562: 최댓값
li = [int(input()) for _ in range(9)]
max = 0
idx = 0
for i, l in enumerate(li):
    if max < l:
        max = l
        idx = i + 1
print(max, idx, sep='\n')