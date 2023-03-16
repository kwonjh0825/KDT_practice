# pr01 : 몫과 나머지 출력하기
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{t} {a//b} {a%b}')

# pr02 : 평균값 구하기
T = int(input())
for t in range(1, T+1):
    li = list(map(int, input().split()))
    print(f'#{t} {round(sum(li)/len(li))}') # 소수점 첫째 자리에서 반올림

# pr03 : 아주 간단한 계산기
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))

# pr04 : 스탬프 찍기
print('#'*int(input()))

# pr05 : 최대수 구하기
T = int(input())
for t in range(1, T+1):
    li = list(map(int, input().split()))
    print(f'#{t} {max(li)}')