# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = dict(zip(keys, values))


# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ? 
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {}
price = 0

while True:
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    family[name] = age
    quit = input('Enter quit when you are finished or press entrer to continue. ')
    if quit == 'quit':
        break

for value in family.values():
    if 3 <= int(value) < 12:
        price += 10
    elif int(value) > 12:
        price += 15 

print (f'The total price for pay: {price}')          

#Exercise 3: Zara
# Here is some information about a brand.

# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        'major_color': {
            'France': 'blue',
            'Spain': 'red',
            'US': ['pink', 'green'],
            }
        } 

# 3. Change the number of stores to 2.

brand['number_stores'] = 2

# 4. Print a sentence that explains who Zaras clients are.
s = ', '.join(brand['type_of_clothes'][0:-1])
print (f'Zara clients are: {s}.')

# 5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# 7. Delete the information about the date of creation.
del brand['creation_date']

# 8. Print the last international competitor.
print (brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US.
print(brand ['major_color']['US'])

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# 11. Print the keys of the dictionary.
print(brand.keys())

# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {'creation_date': 1975, 'number_stores': 10000 }

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
#If my update to adictionary includes an existing key, then the old value is overwritten by the update.
brand.update(more_on_zara)
print(brand)

# 14. Print the value of the key number_stores. What just happened ?
 # Answer: The value was overwritten by the update.


#  Exercise 4 : Disney Characters
# Instructions
# # Use this list :
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {users[i]:i for i in range (len(users))}
print (disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_B = {i:users[i] for i in range (len(users))}
print (disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users.sort()
disney_users_C = {users[i]:i for i in range (len(users))}
print (disney_users_C)


# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users_i = list()
for user in users:
    if 'i' in user:
        users_i.append(user)
disney_users_D  = {users_i[i]:i for i in range (len(users_i))}  
print(disney_users_D)  


# The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users_mp = list()
for user in users:
     if user[0].lower() == 'm' or user[0].lower() == 'p':
         users_mp.append(user)
     
disney_users_E  = {users_mp[i]:i for i in range (len(users_mp))}  
print(disney_users_E) 


