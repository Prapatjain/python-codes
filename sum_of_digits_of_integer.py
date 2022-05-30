n = int(input("Enter your mobile number :"))
sum=0
while(n>0):
    sum=sum+n%10
    n=n//10
print('The sum is :',sum)
