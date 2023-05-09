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
