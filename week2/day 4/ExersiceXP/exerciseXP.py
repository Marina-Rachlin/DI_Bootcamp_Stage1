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
        print('Well done!')
    else:
         print(f'Next time... The numbers are: {number} and {num2}.') 

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

# Make a shirt of any size with a different message.
make_shirt("Small","I love Israel")

# Bonus: Call the function make_shirt() using keyword arguments.
make_shirt(size="Medium", text="We love Python")

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

def make_great(magicians):
    for i in range (len(magicians)):
        magicians[i] = 'The Great '  + magicians[i]

make_great(magician_names)      
show_magicians(magician_names)


# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

 # get_random() 
def get_random_temp():
     return  random.randint(-10, 40)

print(get_random_temp())

# main()
def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius.')


#  main() with more functionality
def main():
    temp = get_random_temp()
    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= temp < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 <= temp < 23:
       print('Spring breeze')
    elif  23 <= temp < 32:
        print('Lets go to the see!')
    else:
        print('Where is the conditioner???')

main()

# changed the get_random(). Added season parameter
def get_random_temp(season):
     if season == 'winter':
         return random.randint(-10, 16)
     elif season == 'spring':
         return random.randint(4, 22)
     elif season == 'summer':
         return random.randint(22, 40)
     else:
         return random.randint(4, 27)
     
# changed the main(). Asking a user about the season.
def main():
    season = input('Please enter a season: winter, spring, summer, fall  ')
    temp = get_random_temp(season)
    if temp < 0:
        print(f'The temperature right now is {temp} degrees Celsius.Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= temp < 16:
        print(f'The temperature right now is {temp} degrees Celsius. Quite chilly! Don’t forget your coat')
    elif 16 <= temp < 23:
       print(f'The temperature right now is {temp} degrees Celsius. Spring breeze')
    elif  23 <= temp < 32:
        print(f'The temperature right now is {temp} degrees Celsius. Lets go to the see!')
    else:
        print(f'The temperature right now is {temp} degrees Celsius.Where is the conditioner???')

#Give the temperature as a floating-point number instead of an integer
def get_random_temp(season):
     if season == 'winter':
         return round(random.uniform(- 10.0, 16.0), 2)  
     elif season == 'spring':
         return round(random.uniform(4.0, 22.0), 2)    
     elif season == 'summer':
         return round(random.uniform(22.0, 40.0), 2)  
     else:
         return round(random.uniform(4.0, 27.0), 2)   

main()

# Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

def main():
    num = int(input('Please enter a number of month: 1 = January, 12 = December  '))
    if 3 <= num <= 5:
        season = 'spring'
    elif 6 <= num <= 8:
        season = 'summer'
    elif  9 <= num <= 11:
        season = 'fall'
    else:
        season = 'winter'
    temp = get_random_temp(season)
    if temp < 0:
        print(f'The temperature right now is {temp} degrees Celsius.Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= temp < 16:
        print(f'The temperature right now is {temp} degrees Celsius. Quite chilly! Don’t forget your coat')
    elif 16 <= temp < 23:
       print(f'The temperature right now is {temp} degrees Celsius. Spring breeze')
    elif  23 <= temp < 32:
        print(f'The temperature right now is {temp} degrees Celsius. Lets go to the see!')
    else:
        print(f'The temperature right now is {temp} degrees Celsius.Where is the conditioner???')

main()     
         
     
