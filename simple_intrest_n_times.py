n=int(input('Enter the times you want to do the operation :'))
for i in range(0,n,1):
    p=int(input('Enter Principal amount :'))
    r=int(input('Enter rate amount :'))
    t=int(input('Enter time amount :'))
    ans=(p*r*t)/100
    print('Simple intrest is :',ans)
