from func import add
import random
import string
import datetime
from faker import Faker

# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn

# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

def roll_and_check(input_number):
    if 1 <= input_number <= 100:
        random_number = random.randint(1, 100)
        if random_number == input_number:
            print("Success! The random number matches your input.")         
        
# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

def random_str():
    str = ''.join(random.choices(string.ascii_letters, k=5))
    print (str)

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

def show_date():
    print(datetime.date.today())

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def time_until_January():
    current_datetime = datetime.datetime.now()
    next_year = current_datetime.year + 1
    january1st = datetime.datetime(next_year, 1, 1)
    time_left = january1st - current_datetime
    # Extract days, hours, minutes, and seconds from the time difference
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time left until January 1st: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def min_in_life(birthdate):
    current_datetime = datetime.datetime.now()
    lived_time = current_datetime - birthdate
    minutes_lived = lived_time.total_seconds() / 60
    print(f"You have lived for approximately {minutes_lived:.2f} minutes.")

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def time_untill_holiday():
    next_holiday = {"name": "Shavuot",
                    "date": datetime.datetime.strptime("2023/05/26", "%Y/%m/%d"),
                    "time_from_now": datetime.datetime.strptime("2023/05/26", "%Y/%m/%d") - datetime.datetime.now()}
    print(f"Today is {datetime.date.today()}. The next holiday is {next_holiday['name']} and it is in {next_holiday['time_from_now'].days} days and "
        f"{int(next_holiday['time_from_now'].seconds / 3600)} hours")
    
# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

def  calculate_age_on_planets(age_in_seconds):
    earth_year_in_seconds = 31557600
    orbital_periods = {
            'earth': 1.0,
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            }
    age_on_planets = {}
    for planet, orbital_period in orbital_periods.items():
        age_on_planet = age_in_seconds / (earth_year_in_seconds * orbital_period)
        age_on_planets[planet] = round(age_on_planet,2)

    for  planet, age in age_on_planets.items():  
        print(f"On {planet} you are {age} Earth-years old")

# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

users = []
def add_user():
    fake = Faker()
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)
    
add(3,4)
roll_and_check(4)
random_str()
show_date()
time_until_January()
birthdate = datetime.datetime(1992, 1, 7)  # Replace with the user's birthdate
min_in_life(birthdate)
time_untill_holiday()
calculate_age_on_planets(1000000000)
for _ in range(5):
    add_user()
for user in users:
    print(user)




