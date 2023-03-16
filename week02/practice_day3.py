# pr01
num = int(input('정수를 입력하세요 > '))
print(-num if num < 0 else num)

# pr02
number_list = [x for x in range(1, 6)]      # [1, 2, 3, 4, 5]
cnt = 0
for number in number_list:
    cnt += 1
print(cnt)

# pr03
number_list = [x for x in range(1, 6)]      # [1, 2, 3, 4, 5]
result = 0
for number in number_list:
    result += number
print(result)

# pr04
number_list = [x for x in range(2, 7, 2)]   # [2, 4, 6]
sum = cnt = 0
for number in number_list:
    cnt += 1
    sum += number
print(sum/cnt)

# pr05
number_list = [x for x in range(1, 6)]      # [1, 2, 3, 4, 5]
result = 1
for number in number_list:
    result *= number
print(result)

# pr06
number_list = [x for x in range(1, 6)]      # [1, 2, 3, 4, 5]
result = number_list[0]
for number in number_list[1:]:
    result = number if number > result else result
print(result)

# pr07
number_list = [x for x in range(1, 6)]      # [1, 2, 3, 4, 5]
result = number_list[0]
for number in number_list[1:]:
    result = number if number < result else result
print(result)