n = int(input('Enter number to swap 1st and last digit :'))
l=n%10
temp=n
count=0
while(temp>10):
    temp=temp//10
    n1=temp%10
    count=count+1
n=n-l
n=n+n1
n=n-(n1*(10**count))
n=n+(l*(10**count))
print(n)
