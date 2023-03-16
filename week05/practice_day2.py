import sys, heapq

# pr01. 10817: 세 수
li = list(map(int, input().split()))
print(sorted(li)[1])

# pr02. 20001: 고무오리 디버깅
input()
pro = 0
while True:
    string = input()
    if string == '문제':
        pro += 1
    elif string == '고무오리':
        if pro:
            pro -= 1
        else:
            pro += 2
    else:
        break
if pro:
    print('힝구')
else:
    print('고무오리야 사랑해')

# pr03. 1269: 대칭 차집합
_, _ = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

a_b = a - b
b_a = b - a
print(len(a_b)+len(b_a))

# pr04. 3052: 나머지
li = set()

for _ in range(10):
    li.add(int(input())%42)
print(len(li))

# pr05. 1181: 단어 정렬
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(sys.stdin.readline().strip())
li = set(li)
print(*sorted(li, key=lambda x: (len(x), x)), sep='\n')

# pr06. 11286: 절댓값 힙
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0: 
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))