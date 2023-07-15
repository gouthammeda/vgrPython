# try creating databricks account
a = 10
b = 2

# arithmetic operator
print('a+b', a + b)
print('a-b', a - b)
print('a*b', a * b)
print('a%b', a % b)
print('a/b', a / b)
print('a//b', a // b)
print('a**b', a ** b)

a = 10.5
b = 2
print('a+b', a + b)
print('a-b', a - b)
print('a*b', a * b)
print('a%b', a % b)
print('a/b', a / b)
print('a//b', a // b)
print('a**b', a ** b)

a = 20.5
b = 20
print("a>b is ", a > b)  # True
print("a>=b is ", a >= b)  # True
print("a<b is ", a < b)  # False
print("a<=b is ", a <= b)  # False

# relational operator
print(True > True)  # False
print(True >= True)  # True
print(True < False)  # False
print(True <= False)  # False

print(10 < 20)  # True
print(10 < 20 < 30)  # True
print(10 < 20 < 30 < 40)  # True
print(10 < 20 > 30 < 40 < 50 < 60)  # False

# Equality operator
print("-----")
print(10 == 20)
print(10 != 20)
print(10 == True)
print(False == False)
print("vgr" == "vgr")
print(10 == 20 == 30 == 401 == 0 == 20)
print(10 == 10 == 10 == 10)

# logical operator

# and,or,not
print("-----")
print(True and True)
print(True and False)
print(True or False)
print(not False)

# assignment operator

# we can use assignment operator to assign value to variable.

x = 10
print(x)
x += 10
print(x)
x += 1000
print(x)
x -= 900
print(x)
x *= 10
print(x)

x = 0
for i in range(10):
    x += 10
print(x)

x = 10
for i in range(10):
    x *= 2
print(x)
