# 1.
s="Learning Python Is Very Easy"
s1=s.split()
for i in s1:
  print(i[0],end="")
# output=LPIVE
print("-------")

# 2)
input="python is very easy."
# output=easy
s= input.split()
print("".join(s[-1]))

# 3)input=B4A1D3
# output=ABD134
print("-----")
s="B4A1D3"
g=[]
p=[]
for i in s:
    if i.isalpha():
        g+=i
    else:
        if i.isdigit():
            p+=i
print("".join(sorted(g)+sorted(p)))

# 4)input=a4b3c2
# output=aaaabbbcc

new_input = ("a"*4)+("b"*3)+("c"*2)
print(new_input)

# 5)
input="AAAQBBBCCCAAADDDCCCBBB"
# OUTPUT=ABCDQ
new_input= set(input)
print("".join(sorted(new_input)))

# 6)
s="AAAQBBBCCCAAADDDCCCBBB"
# OUTPUT:A-6,B-6,C-6,D-3,Q-1
print("A-",s.count("A"),"B-",s.count("B"),'C-',s.count("c"),'D-',s.count("D"),'Q-',s.count('Q'))

# 7)
INPUT="one two three four five six seven"
input=123456
input1=str(123456)
print(input1[::-1])
