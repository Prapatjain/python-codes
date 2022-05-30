size=int(input("enter the size of list:"))
i=0
sum=0
lst=[]
while(i<size):
    x=int(input())
    lst.append(x)
    if(lst[i]<0):
        sum=sum+lst[i]
    i+=1
print("the sum of all negative number is:%d"%sum)
