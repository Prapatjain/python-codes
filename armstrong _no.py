import math
num=int(input("enter the number:"))
temp=num
sum=0
dig=math.log10(num)+1
print(dig)
while(num>0):
    rem=num%10
    sum=sum+(rem**int(dig))
    print(sum,rem)
    num=num//10
if(sum==temp):
    print("armstrong")
else:
    print("not")
