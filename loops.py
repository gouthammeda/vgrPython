x = 'vgrinfotech'
for i in x:
    print(i)

for i in range(10):
    print(i + 1)

z = 0
for i in x:
    print("the index value is :", z, "and value is ", i)
    z += 1

for i in range(100):
    if i % 2 == 0:
        print("This is even number:", i)
    # else:
    #     print("This is odd number:",i)

l1 = []
l2 = []

for i in range(100):
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)

print("this is even numbers is:", l1)
print("this is odd numbers is", l2)
print("------")

l = [1,2,3,4,5,6,7,8,9,10]
x=0
for i in l:
    x= x+i

print(x)

print("------")



sum=0
x=1
while x <= 10:
    print(x)
    sum=x+sum
    x = x+1
print(sum)

# n = int(input("Enter number: "))
# sum=0
# i=1
# while i <= n:
#     sum = sum+i
#     i = i + 1
# print("the sum of first",n,"numbers is:",sum)


# n=int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     print("* "*i)
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("* "*i)
















