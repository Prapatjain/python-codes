#check hamming distance between two numbers.
a=int(input('Enter a number: '))
b=int(input('Enter a number: '))
c=a^b
d=bin(c)
x=0
for i in range(0,len(d)):
    if d[i]=='1':
        x=x+1
print(x)
