# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

import random


def display_message():
    """The function prints one sentence telling everyone what you are learning in this course"""
    print("In this course we learm Javascript, Python, React etc.") 

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f'One of my favorite books is "{title}".')
favorite_book('The Arch of Triumph')    

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country = 'US'):
    print(f'{city} is in {country}.')
describe_city('Tokio', 'Japan')    


# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

def num_compare(number):
    num2= random.randint(0, 100)
    if number == num2:
        print('success message')
    else:
         print(f'fail message. The numbers are: {number} and {num2}.') 

num_compare(13)       


# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt(size, text):
    print(f'The size of the shirt is {size} and the text is: {text}.')

make_shirt('xs', 'never stop learning') 

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
def make_shirt(size = 'large', text = 'I love Python'):
    print(f'The size of the shirt is {size} and the text is: {text}.')

make_shirt() 

# Make medium shirt with the default message
make_shirt(size = 'medium') 

# Make a shirt of any size with a different message./ TODO

# Bonus: Call the function make_shirt() using keyword arguments./TODO

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magicians):
    for magician in magicians:            
        print(magician) 

show_magicians(magician_names)

  
