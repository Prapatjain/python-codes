n = int(input("Enter any three digit number :"))
sum=0
while(n>0):
    if(n>99):
        sum=sum+n%10
        n=n//10
    if(n<10):
        sum=sum+n
        n=n//10
    else:
        n=n//10
print('The sum of 1st and 3rd digit is :',sum)
