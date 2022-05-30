num=int(input("enter the number:"))
i=1
while(i<=10):
    print("%d   X   %d  =   %d"%(i,num,i*num))
    i+=1
#solution4
num=int(input("enter the 10 digit number:"))
i=10
sumodd=0
sumeven=0
while(i>=0):
    if(i%2==0):
        rem=num%10
        sumodd=sumodd+rem
        num=num//10
        i-=1
    else:
        rem=num%10
        sumeven=sumeven+rem
        num=num//10
        i-=1 
if(sumodd==sumeven):
    print("magic")
else:
    print("not")
