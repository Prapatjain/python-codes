message='Hello world'
print(message[0:5])#slicing
print(len(message))#length of a string
print(message.lower())#turn string to lower case
print(message.upper())#turn string to upper case
print(str(message.count('Hello'))+' '+str(message.count('l')))#count a character or substring in string
print(message.find("world"))#find index of any sub-string in string
new_message=print(message.replace('world','universe'))#replace a sub-string with another
print(message)#yet it remains unchanged
message=message.replace('world','universe')#changing the original string
print(message)#not it is changed
word1='My'#declare a string
word2='name'#another declaration
message='{}, {} is Devansh !'.format(word1,word2)#formatting to write a string
print(message)#it is changed again
message=f'{word1}, {word2} is Devansh !'#F-string feature
print(message)#it is printed again
message=f'{word1.lower()}, {word2.upper()} is Devansh !'#F-string feature
print(message)#it is printed again
print(dir(word1))#gives all the functions we can use with the data type(string in this case)
print(help(str))#tells us about each and every function we can use with a data type(string in this case)
print(help(str.lower))#helps us to get information about any function;
