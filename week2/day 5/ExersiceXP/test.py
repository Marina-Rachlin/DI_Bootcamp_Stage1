import random

#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.

s = input('Please enter the 10 characters long string...')
if(len(s) < 10):
    print('String not long enough')
elif(len(s)> 10):
    print('String too long')

 #Then, print the first and last characters of the given text.

print(s[0], s[9])

#Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed.
for i in range(len(s)):
    print(s[:i+1])

#Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). 

l = list(s)
random.shuffle(l)
result = ''.join(l)
print(result)