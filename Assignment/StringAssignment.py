# 1.reverse a string with and without using functions
s="vgr"
print(s[::-1])
print("".join(reversed(s)))
s1=""

for c in s:
    s1=c+s1
print(s1)

# 2. reverse the word in a given string.
s="learning python is very easy"
s1=[]
for i in s.split():
    s1.append(i)

print("".join(s1[::-1]))

# 3. write a program to execute odd and even position of a given string
s="learning python is very easy"
i=0
for c in s:
    print("the positive index is:",i,"negative index is:",i-len(s),"for this character",c)
    i+=1

# 4. program to merge characters of 2 strings into a single string by taking characters alternatively
# s1="ravi",s2="teja"
#output=rtaevjia

s1="ravi"
s2="teja"
s3=""

s.split("")
