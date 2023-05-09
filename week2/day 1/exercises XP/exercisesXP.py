#exercise 1. Print the following output in one line of code:

s = 'Hello World\n' * 4
print(s)

#exercise 2. Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

res = (99**3)*8
print(res)

#exercise 3.
#Predict the output of the following code snippets:
#>>> 5 < 3
#>>> 3 == 3
#>>> 3 == "3"
#>>> "3" > 3
#>>> "Hello" == "hello"

False
True
False
Error
False


#exercise 4. Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = 'Mac'
print(f"I have a {computer_brand} computer.")


#exercise 5. 
# Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
#Have your code print the info message.
#Run your code

name = 'marina'
age = 31
shoe_size = 38
info = 'My name is '+ name + ' i am ' + str(age) + ' years old' + ' and my size of shoes is: ' + str(shoe_size)
print(info)

#exercise 6 
#Create two variables, a and b.
#Each variable value should be a number.
#If a is bigger then b, have your code print Hello World.

a = 5
b = 3
if(a>b):
    print ('Hello World')

#exercise 7
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input('please inter the number and i will tell you whether this number is odd or even.'))
if (num)%2 == 0:
    print (f'{num} is even.')
else:
    print (f'{num} is odd.')

#exercise 8   
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name = 'marina' 
user_name = input('what is your name...')
if(my_name == user_name):
    print('oh! we have the same name!')
else:
    print('you have a very beautiful name')

#exercise 9
#Write code that will ask the user for their height in inches.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.

height = float(input('what is your height in inch...?'))
convert_height =int(height * 2.54) 
if(convert_height > 145):
    print('You are tall enough to ride a roller coaster')
else:
    print('You need to grow some more to ride a roller coaster')
