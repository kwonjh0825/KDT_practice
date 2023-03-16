from datetime import datetime

# pr01
cnt = 0
for s in input('문자열을 입력하세요 > '): 
    if s == 'e':
        cnt += 1
print(cnt)

# pr02
cnt = 0
vowel = ['a', 'e', 'i', 'o', 'u']
for s in input('문자열을 입력하세요 > ').lower():
    if s in vowel:
        cnt += 1
print(cnt)

# pr03
dict_variable = {
    '이름': '권준혁',
    '생년월일': '19970825',
    '회사': '무직',
}

year = int(dict_variable['생년월일'][:4])
now_year = datetime.now().year
print(f'나이 : {now_year-year+1}')

# pr04
dict_variable = {}
dict_variable['이름'] = input('이름을 입력하세요 > ')
dict_variable['전화번호'] = input('전화번호를 입력하세요 > ')
dict_variable['거주지'] = input('거주지를 입력하세요 > ')
print(dict_variable)
print(f'이름 : {dict_variable["이름"]}')
print(f'전화번호 : {dict_variable["전화번호"]}')
print(f'거주지 : {dict_variable["거주지"]}')

# pr05
dict_variable = {}
name = input('이름을 입력하세요 > ') 
dict_variable[name] = {}
dict_variable[name]['전화번호'] = input('전화번호를 입력하세요 > ')
dict_variable[name]['이메일'] = input('이메일을 입력하세요 > ')
dict_variable[name]['거주지'] = input('거주지를 입력하세요 > ')
print(dict_variable)

# pr06
dict_string = {}
string = input('문자열을 입력하세요 > ')
for s in string:
    if s not in dict_string:
        dict_string[s] = 1
    else:
        dict_string[s] += 1

for key, value in dict_string.items():
    print(key, value)