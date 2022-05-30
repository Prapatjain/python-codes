f=open('avin.txt','r')
f1=open("a.txt","w+")
str=f.readlines()
print(str)
for i in range(len(str)):
    if i%2==0:
        print(str[i])
        f1.write(str[i])
        f1.write("\n")
f1.seek(0,0)
a=f1.read()
print(a)
f1.close()
f.close()"""
#sol 2
"""f=open('avin.txt','r')
f1=open('a.txt','w+')
str=f.read().split()
print(str)
for i in range(len(str)):
    if i%2==0:
       print(str[i])
       f1.write(str[i])
       f1.write(' ')
f1.seek(0,0)
a=f1.read()
print(a)
f1.close()
f.close()"""
#sol 3
"""f=open('avin.txt','r')
s=n=t=0
str=f.read()
for i in str:
    if ord(i)==32:
        s+=1
    elif i=='\n':
        n+=1
    elif i=='\t':
        t+=1
print(s,n,t)
f.close()"""

















#assingnment number 1(module2):
#--------------------------------------->>>
#question1::::describe the following method:
#1>fromkeys
#2>setdefault

#question2:::wap to count the frequency of each character in a given string
#expected from the user using dictionary


#question3:::wap to accept rollno,name,and marks of 5 students
#and store the detail in dictionary using roll no as key
#and also display th sum of marks of all five student
#-------------------------------------------->>>


#---------------------------------------------->>>
#question1:>>>ek dictionary use se enter karni hai and find
#the sum of values

#question2:>>ek dict enter karo or values ko sort
#kardo ek list mein


#question3:>>do dict user se enter karani hai or 
#unko marge ek third dict mein
#--------------------------------------------->>>>.
"""dict={}
size=int(input("enter the size od dict:"))
for i in range (size):
    k=input()
    v=int(input())
    dict.update({k:v})
print(dict)
print(dict.values())
print(dict.keys())
print(dict.items())
print(sum(dict.values()))"""
#---------------------------------------->>>>
#solution1:------->>>
"""dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=input()
    values=int(input())
    dict.update({keys:values})
print(dict)
print("sum of all the values is:",end='')
print(sum(dict.values()))"""
#solution2-------------->>>
"""dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
print(sorted(dict.values()))"""
#solution3------------------->>
"""dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
dict1={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict1.update({keys:values})
print(dict1)

dict2={}
for i in (dict,dict1):
    dict2.update(i)
print(dict2)"""

#question4:values ka sum using for loop


#question5:check wether the key is present in the dict or not
#if present the print its value else print
#key not found

#question6
#n====>
#output:d={1:1*5,2:2*5.......}

#question7:print the multiplicayion of all keys and values
#solution4------------------------>
"""dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
sum=0
for i in dict.values():
    sum=sum+i
print(sum)"""
#solution5---------------->>>
"""dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
check=int(input("enter the key which u want to check:"))
if check in dict.keys():
    print(dict[check])
else:
    print("key not found!")"""
#solution7:-------------------------->
dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)










#question 4:total number of lines in a file
"""f=open('avin.txt','r')
f.seek(0,0)
sum=0
str=f.read()
print(str)
for i in str:
    if i=='\n':
        sum+=1
print(sum)
f.close()"""
#question 5: total number of words
"""f=open('avin.txt','r')
f.seek(0,0)
sum=0
str=f.read()
a=str.split()
print(a,type(a))
for i in a:
    sum+=1
print(sum)
f.close()"""
#question 6:total number of characters kitne hai
"""f=open('avin.txt','r')

sum=0
str=f.read()
f.seek(0,0)
for i in str:
    sum+=1
print(sum-1)
f.close()"""
#question 7:to and the ka count kitna hai
"""f=open('avin.txt','r')
f.seek(0,0)
str=f.read()
print(str)
b=str.lower()
print(b)
b=b.split()
print(b)
sum=0
for i in b:
    if i =='to' or i=='and' or i=='the':
            sum+=1
print(sum)
f.close()"""
f=open('avin.txt','r')
str=f.readlines()
print(str,type(str))
