l = [10, "yuvraj", True, "vgr", 20.5, 10, 20, "vgr"]
print(l)
print(l[0])
print(l[-1])
print(l[-5])
print(l[6])
print(l[::-1])
print(l[:2:-2])
print(l[::])
print(l[::1])
# it will return elements starting from zero and ending with 7 and skipping 2 elements in between
print(l[0:7:3])

l.append(100)
print(l)

listt = [0, 1, 2, 3, 4, 'vgr']
print(listt)
# append adds element to the end of list
listt.append("A")
listt.append("B")
print(listt)

# insert adds the value at required index and the existing element will shift one position after element is added.
n = [1, 2, 3, 4, 5]
print(n)
n.insert(1, 1000)
print(n)

l1 = ["KF", "KO", "BD"]
l2 = ["chicken", "mutton", "fish"]

print(l1)
print(l2)
# add elements of l2 into l1.
l1.extend(l2)
print(l1)

# add elements of l1 into l2.
l2.extend(l1)
print(l2)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(l)

# removes the specified element from the list
l.remove(1)
print(l)

# removes last element of the list.
ls = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(ls.pop())
# removes the first element from the list.
print(ls.pop(1))

n = [100, 10, 90, 30, 40, 20]
n.reverse()
print(n)

n = ["bananna", "apple", "mango", "graps"]
print(n)
n.sort()
print(n)

n = ["bananna", "apple", "mango", "graps"]
print(n)
n.sort()
print(n)
n.sort(reverse=True)
print(n)

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = l1.copy()
print(l2)

# concatenate lists
l1 = [10, 20, 30, 40, 50]
l2 = [100, 200, 300, 400]
print(l1 + l2)


l1=[1,2,3,4,5]
l2=[10,20,30,40,50,100]
print(l1==l2)
print(l1!=l2)
print(l1>l2)
print(l1<l2)
# clears the list and returns the value.
l1.clear()
print(l1)

l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
for i in l:
    print(i)
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
print("---")

l=[[10,20,30],[40,50,60],[70,80,90]]
res=[]
print(l)
for i in l:
    print(i)
for i in l:
    for j in i:
        res.append(j)

print(res)

# List comprehensions
l=[x*x for x in range(1,11)]
print(l)

l=[1,2,3,4,5,6,7,8,9,10]
lt=[x for x in l if x%2==0]
print(lt)

lt=[x for x in l if x%2!=0]
print(lt)

names=["Yuvaraj","Monika","Priya","Suresh"]
l=[w[0] for w in names]
print(l)

l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[i for i in l1 if i not in l2]
print(l3)