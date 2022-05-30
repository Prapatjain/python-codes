lst=[]
lst2=[]
for i in range (2):
    lst1=[]
    for j in range (2):
        lst1.append(int(input()))
    lst.append(lst1)
print("enter the elements of list second:")
lst3=[]
for i in range (2):
    lst4=[]
    for j in range (2):
        lst4.append(int(input()))
    lst3.append(lst4)
print("list 1 is:")
for i in range (2):
    for j in range (2):
            print(lst[i][j],end='')
    print()
print("list 2 is:")
for i in range (2):
    for j in range (2):
        print(lst3[i][j],end='')
    print()
lst9=[]
print("the matrix after the multiplication:")
for i in range (2):
    for j in range (2):
        lst9
