# pr01
string = input('문자열을 입력하세요 > ')
for i, s in enumerate(string):
    if s == 'e':
        print(i)
        break
else:
    print(-1)

# pr02
str_list = list(input('문자열을 입력하세요 > ').split())
str_dict = {}
for string in str_list:
    str_dict[string] = str_dict.get(string, 0) + 1

for key, value in str_dict.items():
    print(key, value)


# pr03
string = input('문자열을 입력하세요 > ')
ans = '' 
for s in string:
    if s != 'e':
        ans += s
print(ans)

# pr04
string, a = input('문자열을 입력하세요 > ').split()
cnt = 0
for s in string:
    if s == a:
        cnt += 1
print(cnt)

# pr05
a, b, c = input('문자열을 입력하세요 > ').split()
print(f'{a}-{b}-{c}')

# pr06
number = int(input('문자열을 입력하세요 > '))
sum = 0
if number < 0:
    print(-1)
else:
    while number:
        sum += (number % 10)
        number = number // 10
    print(sum)
