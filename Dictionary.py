d={1:"yuvraj"}
print(d)
print(type(d))
# we can add elements into a dictionary
d[101]="vgr"
print(d)
d= {1:'yuvraj',True:100,'raju':1000}
print(d)

# keys can't be duplicate, values can be duplicate and picks up latest value in result when keys are duplicate
d={1:"yuvaraj",2:"yuvaraj",3:"yuvaraj","lavanya":100,1:"yuvraj1",2:"yuvraj3"}
print(d)

d= {1:"sujay",2:"goutham",3:"yuvraj",4:"sujay",5:"sujay"}
print(d)

d={}
d[100]="vgr"
d[200]="adithi"
d[300]="deepika"
print(d)

d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
d[100]="infotech"
print(d)
d[300]="lavanya"
print(d)

# delete element in dictionary
d= {1:"sujay",2:"goutham",3:"yuvraj",4:"sujay",5:"sujay"}
del d[1]
print(d)
del d[5]
print(d)

# clears element in the dictionary
d= {1:"sujay",2:"goutham",3:"yuvraj",4:"sujay",5:"sujay"}
d.clear()
print(d)

d= {1:"sujay",2:"goutham",3:"yuvraj",4:"sujay",5:"sujay"}
print(len(d))
print(d.get(2))
print(d.get(5))

# using pop method
d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
print(d.pop(100))
d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
print(d.pop(100))
# value doesn't exist it will throw error.
# print(d.pop(500))


d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d)


d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
print(d.keys())
print(sum(d.keys()))

d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
print(d.values())
# print(sum(d.values()))

for k,v in d.items():
    print(k,"-----",v)

# getting sum of keys and values
d={1:100,2:200,3:300,4:400}
print(d)
x=0
res_k=0
res_v=0
for k,v in d.items():
    res_k=k+res_k
    res_v=v+res_v
print(res_k)
print(res_v)

# copying the dictionary
d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d)
d1=d.copy()
print(d1)

d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d.setdefault(200))

# set default if already key value exist then no change if it doesn't exist then adds the value.
d={100: 'vgr', 200: 'adithi', 300: 'deepika'}
print(d.setdefault(200,"yuvaraj"))
print(d)
print(d.setdefault(400,"yuvaraj"))
print(d)

# square:Dict Comprehension
sq={x:x*x for x in range(1,10)}
print(sq)

lt=[100,200,300,400,500,600,700,800,900,1000]
d={x:lt[x] for x in range(0,len(lt))}
print(d)


