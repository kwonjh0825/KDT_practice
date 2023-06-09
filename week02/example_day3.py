# ex01 
list_variable = [x for x in range(7)]       # [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=' ')
print()
'''
2 3 4 5 7 8
'''

# ex02 
for element in range(-2, 10, 2):
    print(element, end=' ')
print()

'''
-2 0 2 4 6 8
'''

# ex03
a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1

    if number % 3 == 0:
        b = b + 1

    if number % 4 == 0:
        c = c + 1

    if number % 5 == 0:
        d = d + 1
print(a, b, c, d)       # 5 4 3 2

# ex04
i = 0
while i<= 10:
    print(i)
    i = i + 1
'''
0
1
2
3
4
5
6
7
8
9
10
'''

# ex05
i = 0
while i<= 10:
    i = i + 1
    print(i)
'''
1
2
3
4
5
6
7
8
9
10
11
'''

# ex06
i = 0
while i<= 10:
    i = i + 2
    print(i)
'''
2
4
6
8
10
12
'''

# ex07
i = 0 
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
'''
0
1
2
3
4
5
6
7
8
9
10
'''

# ex08
i = 0 
while True:
    print(i)
    if i > 10:
        break
    i = i + 1
'''
0
1
2
3
4
5
6
7
8
9
10
11
'''

# ex09
list_variable = [x for x in range(7)]       # [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable))       # 7


# ex10
list_variable = [x for x in range(7)]       # [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable))       # 21