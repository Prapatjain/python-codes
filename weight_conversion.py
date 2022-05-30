weight=int(input('Enter your weight : '))
typ=input('Is it in (K)kg or (G)gram :')
if typ=='K':
    print("Your weight in gram is : " + str(weight*1000))
else:
    print('Your weight in kg is : ' + str(weight/1000))      
