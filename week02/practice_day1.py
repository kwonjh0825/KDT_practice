# pr01
num = int(input('숫자를 입력해주세요 > '))
print(num+10)

# pr02
food = input('좋아하는 음식을 입력해 주세요 > ')
print(f'좋아하는 음식 : {food}')

# pr03
name = input('이름을 입력해주세요 > ')
year = int(input('태어난 년도를 입력해주세요 > '))
print(f'저의 이름은 {name}이고, 올해 나이는 {2023-year+1}세 입니다')    # 한국식 나이

# pr04
string1 = input('첫 번째 문장을 입력해주세요 > ')
string2 = input('두 번째 문장을 입력해주세요 > ')
print(string1+string2)

# pr05
num = int(input('숫자를 입력해주세요 > '))
print(-1*num)

# pr06
num1 = int(input('첫 번째 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 숫자를 입력해주세요 > '))
print(f'더하기 연산 : {num1+num2}')
print(f'빼기 연산 : {num1-num2}')
print(f'곱하기 연산 : {num1*num2}')
print(f'몫 연산 : {num1//num2}')
print(f'나머지 연산 : {num1%num2}')

# pr07
num1 = int(input('첫 번째 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 숫자를 입력해주세요 > '))
num3 = int(input('세 번째 숫자를 입력해주세요 > '))
print((num1+num2+num3)/3)

# pr08
li = []
li.append(int(input('첫 번째 숫자를 입력해주세요 > ')))
li.append(int(input('두 번째 숫자를 입력해주세요 > ')))
li.append(int(input('세 번째 숫자를 입력해주세요 > ')))
li.append(int(input('네 번째 숫자를 입력해주세요 > ')))
li.append(int(input('다섯 번째 숫자를 입력해주세요 > ')))
print(li)

# pr08_v2
li = []
for i in range(1, 6):
    li.append(int(input(f'{i} 번째 숫자를 입력해 주세요 > ')))
print(li)

# pr09
string = input('문자열을 입력해주세요 > ')
num = int(input('숫자를 입력해주세요 > '))
print(string*num)

# pr10
sum = 0
sum += int(input('첫 번째 숫자를 입력해주세요 > '))
print(sum)
sum += int(input('두 번째 숫자를 입력해주세요 > '))
print(sum)
sum += int(input('세 번째 숫자를 입력해주세요 > '))
print(sum)
sum += int(input('네 번째 숫자를 입력해주세요 > '))
print(sum)
sum += int(input('다섯 번째 숫자를 입력해주세요 > '))
print(sum)

# pr10_v2
sum = 0
for i in range(1, 6):
    sum += int(input(f'{i} 번째 숫자를 입력해주세요 > '))
    print(sum)