# ex01. 2789: 유학 금지
name = input()
string = 'CAMBRIDGE'
ans = ''
for n in name:
    if n not in string:
        ans += n
print(ans)

# ex02. 2675: 문자열 반복
N = int(input())

for _ in range(N):
    p, string = input().split()
    p = int(p)
    for s in string:
        print(s*p, end='')
    print()

# ex03. 10988: 팰린드롬인지 확인하기
string = input()
print(1) if string == string[::-1] else print(0)

# ex04. 17249: 태보태보 총난타
punch = list(input().split('(^0^)'))
for p in punch:
    print(p.count('@'), end=' ')

# ex05. 2941: 크로아티아 알파벳
a = input()
cro_alpha = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro_alpha:
    a = a.replace(i, "*")
print(len(a))

# ex06. 10809: 알파벳 찾기
string = input()
alpha = [-1] * 26
for i, s in enumerate(string):
    if alpha[ord(s)-97] == -1:
        alpha[ord(s)-97] = i
print(*alpha)
