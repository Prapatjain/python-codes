d={}
x=int(input("Enter the size :"))
for i in range (0,x,1):
    k=input("Enter key :")
    v=input("Enter value :")
    d.update({k:v})
add=0
for i in d:
    add=add+int(i)
print(d.keys())
print(add)
