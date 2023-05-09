# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

num =int(input('Please enter the number '))
lenght = int(input('Please enter the lenght '))
l = []
for  x in range (1, lenght +1):
    l.append(num * x)
print(l)   

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

str = input('Please enter the string ')
new_str = str[0]

for i in range (1, len(str)):
    if str[i] != str[i-1]:
        new_str += str[i]
print (new_str)      