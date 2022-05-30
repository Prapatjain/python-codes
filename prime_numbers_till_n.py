n = int(input('Enter till where you want prime numbers :'))
for i in range(1,n+1,1):
    temp=i
    temp2=0
    for j in range(2,i,1):
        if(temp%j==0):
            temp2=0
            break
        else:
            temp2=1
    if(temp2==1):
        print(i)
    temp2=0
