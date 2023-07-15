x1=int(input("enter n the first value   :"))
x2=int(input("enter n the second value   :"))
print(x1+x2)  #30
print(type(x1))
print(type(x2))


# name = input("Enter name: ")
# if name == "vgr":
#     print("Hello vgr Good morning")
# else:
#     print("hello guest good morning")
# print("how are you")

n1=int(input("enter first number :"))
n2=int(input("enter second number :"))
n3=int(input("enter third number :"))
if n1>n2 and n1>n3:
	print("biggest number is :",n1)
elif n2>n3:
	print("biggest number is :",n2)
else:
	print("biggest number is :",n3)


n=int(input("Enter a digit from 0 to 9 :"))
if n==0:
	print("Zero")
elif n==1:
	print("One")
elif n==2:
	print("two")
elif n==3:
	print("Three")
elif n==4:
	print("four")
elif n==5:
	print("Five")
elif n==6:
	print("six")
elif n==7:
	print("seven")
elif n==8:
	print("eight")
elif n==9:
	print("nine")