# ex01
number1 = 1
number2 = number1 + 1
print(number1, number2) # 1 2

# ex02
number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2
print(number1, number2, number3, number4) # 10 5 105 15

# ex03
string1 = 'Hello'
string2 = string1
string3 = 'Wolrd' + '!'
print(string2, '?', string3) # Hello ? World!

# ex04
string = 'Hello?'
n = 5
print(string * n) # Hello?Hello?Hello?Hello?Hello?

# ex05
string = 'abc hello def'
sub_string1 = string[4:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]

print(sub_string1) # hello 
print(sub_string2) # bc 
print(sub_string3) # f

# ex06
number1 = 5
number2 = 10.0 + number1
number1 - 5
number3 = number1 * (number2 + 10)

print(number1, number2, number3) # 5 15.0 125.0

# ex07
list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]
print(sub_list) # 3

# ex08
list_variable = []
list_variable.append(1)
list_variable.append('a')
list_variable[0] = 0
print(list_variable) # [0, 'a']

# ex09
name = input('너의 이름은?') # 권준혁
print(name) # 권준혁

# ex10
age = int(input('너의 나이는?')) # 27
print('올해 나이 : ', age) # 올해 나이 :  27
print('내년 나이 : ', age + 1) # 내년 나이 :  28