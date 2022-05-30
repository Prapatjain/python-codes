size=int(input("enter the size of list:"))
i=0
sum=0
sum2=0
lst=[]
while(i<size):
    x=int(input())
    lst.append(x)
    if(lst[i]%2==0):
        sum=sum+lst[i]
    else:
        sum2=sum2+lst[i]
    i+=1
print("the sum of all even number is:%d"%sum)
print("the sum of all odd number is:%d"%sum2)
