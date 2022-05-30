string=input('Enter the string :')
vowel=digits=space=con=0
for i in range(0,len(string),1):
    if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
        vowel=vowel+1
    elif string[i]=='1' or string[i]=='2' or string[i]=='3' or string[i]=='4' or string[i]=='5' or string[i]=='6' or string[i]=='7' or string[i]=='8' or string[i]=='9' or string[i]=='0':
        digits=digits+1
    elif string[i]==' ':
        space=space+1
    else:
        con=con+1
print('Vowel=',vowel)
print('Consonent=',con)
print('Spaces=',space)
print('Digits=',digits)
