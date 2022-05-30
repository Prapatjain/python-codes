num=int(input())
lst=[]
for i in range(1,11):
    lst.append(i)
lst1=list(map(lambda n1:n1*num,lst))
print(lst1)
