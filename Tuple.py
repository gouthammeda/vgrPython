t=(1,2,3,4,5)
print(t)
print(type(t))
print("------")
words="The quick brown fox jumps over the lazy dog".split()
print(type(words))
t=tuple(words)
print(type(t))
l=list(t)
print(type(l))

t=(10,20,30,40)
print(len(t))

# supports both forward and reverse index.
t=(10,20,30,40,50,60,70,80,90,100)
print(t[0])
print(t[-1])
# print(t[10])

t=(10,20,30,40,50,60,70,80,90,100)
# gets values starting from 2 and between 5 i.e 5 is excluded.
print(t[2:5])
print(t[2:100])
# right to left skip two elements.
print(t[::2])

t=(10,20,30,40,50,60,70,80,90,100)
# t[1]=100

t1=(10,20,30,40,50,60,70,80,90,100)
t2=(1,2,3,4,5,6,7,8,9,10)
print(t2+t1)
print(t2*2)

t1=(10,20,30,40,50,60,70,80,90,100)
print(len(t1))

t=(1,2,3,4,5,1,2,3,4,5,1,2,3)
print(t.count(3))

t=(1,2,3,4,5,1,2,3,4,5,1,2,3,3)
print(t)
t1=sorted(t)
print(t1)
t1=sorted(t,reverse=True)
print(t1)

t=(100,20,10,400,40,50)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t)/len(t))

a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)

fruits=("apple","banana","orange")
(a,b,c)=fruits
print(a)

t=(x**2 for x in range(10))
print(t)
