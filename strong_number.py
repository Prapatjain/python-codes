n = int(input('Enter number you want ro check strong or not :'))
temp=n
sum=0
while(n>0):
    r=n%10
    fact=1
    for i in range(1,r+1,1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==temp):
    print("Yes it is strong number.")
else:
    print('No its not a strong number.')
