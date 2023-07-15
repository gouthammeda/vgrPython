s = "vgr infotech"
# prints values from 1 to 7 of the string.
print(s[1:8])
# print values from 1 to 7 by taking 2nd element in between.
print(s[1:8:2])
print(s[0:11])
print(s[0:11:2])
print(s[0:11:3])
print(s[::3])
print(s[8:11:2])
print(s[::-2])

print("vgr"+"infotech")
print("vgr"+"infotech")

print("vgr"*5)
# print("vgr"+2)

v='vgr infotech'
print(len(v))
print('i' in v)
print('z' in v)

print("-----")
s1="vgr"
s2="infotech"
print(s1!=s2)
print(s1==s2)
print(s1>s2)
print(s1<s2)


# s=input("enter the string  is  : ")
# sub=input("enter sub string is  :  ")
# if sub in s:
#     print(sub,"found in main string")
# else:
#     print(sub,"not found in main string")

s1="vgr"
s2="infotech"
print(s1!=s2)
print(s1==s2)
print(s1>s2)
print(s1<s2)

# country=input("enter the country name  :  ")
# c=country.strip()
# if c=="india":
#     print("Hello india")
# elif c=="china":
#     print('Hello C hines')
# else:
#     print("Hello other countries")


s="learning python is very easy"
# returns the index of p in the above sentence.
print(s.find("python"))
print(s.find("java"))
print(s.find('v'))
print(s.rfind("v"))

# prints occurrence of y between 1 and 20 letters.
print(s.find('y',1,20))

# returns the index value of variable
print("vgr".index("r"))
print("vgr infotech".index("vgr"))
# print("vgr infotech".index("agr"))

s="abca bcabcab cadda"
# counts occurrence of 'a' in the given string
print(s.count("a"))  #6
print(s.count("ab")) #4
print(s.count("a",4,10)) # 2

# replaces old value with new value.
s="abr infotech"
print(s)
print(s.replace("abr","vgr"))

s = "ababababababababa"
print(s.replace("a","z"))

# splitting of string.
s="vgr infotech is a training centre"
print(s)
s1=s.split()
print(type(s1))
for i in s1:
    print(i)

s = '04-07-2023'
s1 = s.split("-")
print(s1)
for i in s1:
    print(i)

# joining of string
t=('sunny','bunny','chinny','kunny')
s="".join(t)
s1="-".join(t)
print(s)




















