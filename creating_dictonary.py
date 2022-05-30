d={}
x=int(input("Enter the size :"))
for i in range (0,x,1):
    k=input("Enter key :")
    v=input("Enter value :")
    d.update({k:v})
print(d)
