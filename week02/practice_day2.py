# ex01 
if int(input('정수를 입력하세요 > ')) > 0:
    print(True)
else: print(False)

# ex01_v2
print(True if int(input('정수를 입력하세요 > ')) > 0 else False)

# ex02
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 == num2:
    print(False)
else:
    print(max(num1, num2))

# ex02_v2
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
print(False if num1 == num2 else max(num1, num2))

# ex03
num = int(input('정수를 입력하세요 > '))
if num < 10 and num > 1:
    print(True)
else: 
    print(False)

# ex03_v2
num = int(input('정수를 입력하세요 > '))
print(True if num < 10 and num > 1 else False)

# ex04
num = int(input('정수를 입력하세요 > '))
if num > 0 and num % 2 == 0:
    print(True)
else: 
    print(False)

# ex04_v2
num = int(input('정수를 입력하세요 > '))
print(True if num > 0 and num % 2 == 0 else False)

# ex05
num = int(input('정수를 입력하세요 > '))
if num > 100 or num < 0:
    print('에러')
elif num > 59:      # 정수를 입력하기 때문에 60이상과 59초과는 같다고 할 수 있음
    print('합격')
else: 
    print('불합격')

# ex06
string = input('문자열을 입력하세요 > ')
for s in string[::-1]:
    print(s)

# ex07
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 == num2:
    print(False)
else:
    for i in range(min(num1, num2) + 1, max(num1, num2)):
        print(i)

# ex08
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 == num2:
    print(False)
else:
    for i in range(max(num1, num2) - 1, min(num1, num2), -1):
        print(i, end=' ')

# ex09
num = int(input('정수를 입력하세요 > '))
if num < 1:
    print(False)
else:
    for i in range(1, num, 2):
        print(i)

# ex10
for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i} X {j} = {i*j}')
