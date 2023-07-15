# converting string to upper or lowercase
s="Vgr Infotech"
print(s.upper())
print(s.lower())
print(s.swapcase())

s='python is very easy programming in the any of api'
# first letter of each word will be in capital words
print(s.title())
# first letter of first word will be capital.
print(s.capitalize())

s="learning python is very easy"
print(s.startswith("learning"))
print(s.endswith("easy"))
print(s.startswith("easy"))

print("----")
print("vgr123".isalnum())
print("vgr123".isalnum())
print("vgr143".isalpha())
print("vgrinfotech".isalpha())
print("vgrinfotech".isdigit())
print("143123".isdigit())
print("vgrinfotech".isupper())
print("VGrInfotech".islower())
print("Vgr".istitle())

print("----")
s="vgr123infotech456"
digit=[]
ch=[]
for i in s:
    if i.isdigit():
        digit.append(i)
        d = "".join(digit)
    else:
        if i.isalpha():
            ch.append(i)
            c="".join(ch)
print(d)
print(c)

name="yuvaraj"
salary=100000
age=30
print("{}'s salary is {} and his age is {}".format(name,salary,age))

# script

import sys
table_name=sys.argv[1]
db_name=sys.argv[2]
property=sys.argv[3]

print("table is {} database is {} and property is {}".format(table_name, db_name, property))















