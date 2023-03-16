# ex01
dict_variable = {}
dict_variable['이름'] = '정우영'
dict_variable['생년월일'] = '19000101'
dict_variable['회사'] = '하이퍼그로스'

print(dict_variable['이름'])        # 정우영
print(dict_variable['생년월일'])     # 19000101
print(dict_variable['회사'])        # 하이퍼그로스

# ex02
dict_variable = {'a': 'A', 'B':'b'}
dict_variable['c'] = 'C'
dict_variable['D'] = 'd'
dict_variable['e'] = 'E'

print(dict_variable['a'])       # A
print(dict_variable['D'])       # d
print(dict_variable['b'])       # KeyError

# ex03
dict_variable = {}
dict_variable['apple'] = 5000
dict_variable['banana'] = 3000
dict_variable['apple'] = 2000
dict_variable['banana'] = dict_variable['banana'] + 1000

print(dict_variable['apple'] + dict_variable['banana'])     # 6000

# ex04
dict_variable = {
    '이름': '정우영',
    '생년월일' : '19000101',
    '회사': '하이퍼그로스', 
}

for key in dict_variable:
    print(key, dict_variable[key])

'''
이름 정우영
생년월일 19000101
회사 하이퍼그로스
'''

# ex05
dict_variable = {
    '이름': '정우영', 
    '생년월일': '19000101',
    '회사': '하이퍼그로스',
}

for key, value in dict_variable.items():
    print(key, value)

'''
이름 정우영
생년월일 19000101
회사 하이퍼그로스
'''

# ex06
dict_variable = {
    '이름': '정우영', 
    '생년월일': '19000101',
    '회사': '하이퍼그로스',
}

print('나이' in dict_variable)      # False

# ex07
dict_variable = {
    '이름': '정우영', 
    '생년월일': '19000101',
    '회사': '하이퍼그로스',
}

if '거주지' not in dict_variable:
    dict_variable['거주지'] = '서울특별시'
    # 위 조건문의 조건식은 dict_variable에 '거주지' 라는 키를 가지고 있는지 물어봄
    # dict_variable에 '거주지' 키가 없다면 '거주지' 키에 '서울특별시'라는 value를 가진 데이터 추가

print(dict_variable)    # {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}

# ex08
list_variable = []
try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])

except:
    print('에러가 발생했습니다.')
    print('에러의 원인은 무엇인가요?')

'''
에러가 발생했습니다.
에러의 원인은 무엇인가요?       # IndexError
'''

# ex09
try:
    number = 1
    if number == 1:
        print(number)
except:
    print('에러가 발생했습니다.')
    print('에러의 원인은 무엇인가요?')

'''
SyntaxError
'''

# ex10
n = 10
total = 0

for number in range(0, n+1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3
print(total)        # 100