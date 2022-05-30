num=int(input("enter the number:"))
temp=num*num
sum=0
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if(sum==num):
    print("the number is neon number!")
else:
    print("the number is not a neon number!")
