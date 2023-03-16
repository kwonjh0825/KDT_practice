import collections, sys

# pr01. 2576: 홀수
num_li = [int(input()) for _ in range(7)]
odd_num = []
for num in num_li:
    if num % 2:
        odd_num.append(num)
if odd_num:
    print(sum(odd_num))
    print(min(odd_num))
else:
    print(-1)

# pr02. 10822: 더하기
print(sum(list(map(int, input().split(',')))))

# pr03. 2754: 학점 계산
score_dict = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7}
print(score_dict.get(input(), 0.0))

# pr04. 5622: 다이얼
dial = {'ABC': 3, 'DEF': 4, 'GHI': 5 , 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
string = input()
time = 0
for s in string:
    for j in dial:
        if s in j:
            time += dial.get(j)
            break

print(time)

# pr05. 2577: 숫자의 개수
num = [int(input()) for _ in range(3)]
result = 1
for n in num:
    result *= n
cnt = collections.Counter(str(result))
for i in range(10):
    print(cnt.get(str(i), 0))

# pr06. 7785: 회사에 있는 사람
n = int(sys.stdin.readline())

work = dict()
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        work[name] = 1
    else:
        work[name] = 0
print(*(sorted([w for w, s in work.items() if s == 1], reverse=True)), sep='\n')

# for w in sorted(work.items(), reverse=True):
#     if w[1] == 1:
#         print(w[0])