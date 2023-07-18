# 1.
l=[1,2,3,4,5,6,7,8,9]

# s=[]
# for i in range(len(l)+1):
#     s.append([l[i],l[i+1]])
#     print(s)

# 2.

l=[1,2,3,4,5,1,2,3,5,3,2,4,1]
s=[]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==5 and (l[i],l[j]) not in s:
            s.append((l[i],l[j]))
print(s)

# 3.
l=[1,2,3,4,5,1,2,0,3,5,3,6,8,2,4,1]

s= []

for x in l:
    if l.count(x)==1:
        s.append(x)
        print(s)

# 4.
l=[100,20,30,80,40]
# output=[20,30,40,80,100]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
            print(l)
            print("second highest maxvalue",l[-2])

# 5.
l=[100,20,90,30,80,40]
print(l)

for i in range(len(l)):
    for j in range(i+2,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[i],l[j]
            print('second maxvalue',l[2])

#  6.
l=[123,345,342,987,12]
b = []
for i in range(len(l)):
    k=str(l[i])
    s=0
    for j in range(len(k)):
        s= s+int(k[j])
    b.append(s)
print(b)


# 7.
l=[10,200,100,"yuvaraj","raju",30,40,10]

s= 0
for a in l:
    if str(a).isdigit():
        s+=a
    print(s)

l1=[1,2,3,4,5,6]
l2=[4,5,6,8,9]
# 0utput:[1,2,3,4,5,6,8,9]

l1.extend(l2)
print(l1)
a=[]
for x in l1:
    if x not in a:
        a.append(x)
        print(a)

