import sys

# pr01. 9498: 시험 성적
n = int(input())

if n >=90:
    print("A")
elif n>=80:
    print("B")
elif n >= 70:
    print("C")
elif n >= 60:
    print("D")
else:
    print("F")

# pr02. 9093: 단어 뒤집기
T = int(sys.stdin.readline())
for _ in range(T):
    li = list(sys.stdin.readline().split())
    for l in li:
        print(l[::-1], end=' ')
    print()

# pr03. 11721: 열 개씩 끊어 출력하기
string = input()
for i in range(0, len(string), 10):
    print(string[i:i+10])

# pr04. 2947: 나무 조각
li = list(map(int, input().split()))
while li != sorted(li):
    for i in range(4):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            print(*li)
