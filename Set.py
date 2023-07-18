# insertion order is not preserved, stores values in random.
s={10,20,"yuvaraj",30,True,10.4,"yuvaraj",10}
print(s)

# duplicate values are not allowed, it stores the unique values.
s={10,20,"yuvaraj",30,True,10.4,"yuvaraj",10}
print(s)

s={10,20}
s.add(30)
s.add(35)
print(s)


s= {10,20}
s.update([10,20,0,400],range(10))
print(s)

# removes one random element in dataset.
s={10,20,30,40,50}
print(s.pop())

s={10,20,30,40,50}
print(s.pop())
print(s.pop())

print(s.pop())

# removes 13 ele from below set.
s={10,20,30,40,100,12,13,14}
s.remove(13)

print(s)

# if element not present it will not throw error.
s.discard(1000)

# duplicate elements are removed in set.
a={10,20,30,40}
b={50,60,70,10,20}
print(a.union(b))

print("-----")
a={10,20,30,40,70}
b={50,60,70,10,30}
print(a.intersection(b))
# print values contain in a
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))

s={x*x for x in range(1,10)}
print(s)



