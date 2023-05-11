#🌟 Exercise 1 : Set
#Instructions
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(6)
my_fav_numbers.add(7)
my_fav_numbers.remove(7)
friend_fav_numbers = { 4,2,8,6,9}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#🌟 Exercise 2: Tuple
#Instructions
#Given a tuple which value is integers, is it possible to add more integers to the tuple?

# Answer
#No, tuples are immutable, we can not change, add, or remove items once the tuple is created. But the member objects may be mutable.

#🌟 Exercise 3: List
#Instructions
#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#Remove “Banana” from the list.
#Remove “Blueberries” from the list.
#Add “Kiwi” to the end of the list.
#Add “Apples” to the beginning of the list.
#Count how many apples are in the basket.
#Empty the basket.
#Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append('Kiwi')
basket.insert(0, 'Apples')
count = basket.count('Apples')
basket.clear()
print(basket)

#🌟 Exercise 4: Floats
#Instructions
#Recap – What is a float? What is the difference between an integer and a float?
#Can you think of another way to generate a sequence of floats?

#Answers
# float is a data type composed of a number that is not an integer, because it includes a fraction represented in decimal format.
# Floats are numbers with adecimal points, ingegers are numbers without decimal point.
# We can generate a sequence of floats by using arange()function of NumPy library. 
# Also we an use Python generators and yield to write a custom function to generate a range of float numbers.
# And I really liked the way I did it below.

#Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# method range() doesn't work for floats. but we can "fool" him, bring our floats to integers (in our case multiple by 10), ask "range" to give us a sequence and then, when we will get the result bring the integers back to their original form (divide by 10.0)
l = [x/10.0 for x in range(15, 55, 5)]
print (l)

#🌟 Exercise 5: For Loop
#Instructions
#Use a for loop to print all numbers from 1 to 20, inclusive.

for i in range(1, 21):
    print(i, end=" ")

#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1, 21):
    if i%2 == 0:
        print(i, end=" ")


#🌟 Exercise 6 : While Loop
#Instructions
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = 'marina'

while True:
    user_name = input('Please enter your name ')
    if(user_name == my_name):
        print(' we have the same name ') #for testing
        break


#🌟 Exercise 7: Favorite Fruits
#Instructions
#Ask the user to input their favorite fruit(s) (one or several fruits).
#Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#Now that we have a list of fruits, ask the user to input a name of any fruit.
#If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruits = input('What is your favorite fruit? (please separate with a space if you have several favirite fruits)')
l = fav_fruits.split(" ")

chosen_fruit = input('What fruit do you want? ')
if chosen_fruit in l:
    print('You chose one of your favorite fruits! Enjoy! ')
else:
    print('You chose a new fruit. I hope you enjoy ')


#Exercise 8: Who Ordered A Pizza ?
#Instructions
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

prompt = "What topping would you like on your pizza? (Enter 'quit' when you are finished) "
l = list()
price = 10
topping = ''
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else: 
        l.append(topping)
        price += 2.5
        print (f'I will add {topping}  to your pizza.')  

print(f'The toppings you chose are : {l}. \nThe total price for pay is: {price}')


#Exercise 9: Cinemax
#Instructions
#1. A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.
#2. Ask a family the age of each person who wants a ticket.
# 3. Store the total cost of all the family’s tickets and print it out.

prompt = "How old are you?\nEnter 'quit' when you are finished."
price = 0

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if 3 <= int(age) < 12:
        price += 10
    elif int(age) > 12:
        price += 15

print  (f'The total price to pay : {price}') 


# Another way using for loop
family = 4 # variable stores the number of persons in the family
price = 0
for i in range (1, family + 1):
    age = input('How old are you? ')
    if 3 <= int(age) < 12:
        price += 10
    elif int(age) > 12:
        price += 15

print  (f'The total price to pay : {price}')  
 
    
#4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.

count = 0 # to count how many elements we delete from the list. When we delete element from the list it immediately affects the numbering(indexes) of remaining elements.
l = ['Marina', 'Mark', 'Liora', 'Adam', 'Pninit', 'Ofir']
for i in range (0, len(l)):
     age = input('How old are you? ')
     if 16 <= int(age) <= 21:
         del(l[i - count])
         count += 1

print(f'The list of teenagers are permitted to watch the movie is : {l}')


#Exercise 10 : Sandwich Orders
#Instructions
#sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

#Use the above list called sandwich_orders.
#Make an empty list called finished_sandwiches.
#As each sandwich is made, move it to the list of finished sandwiches.
#After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f'I made your {sandwich}')


#Exercise 11 : Sandwich Orders#2
#Instructions
#Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
#Make sure no pastrami sandwiches end up in finished_sandwiches.    
 
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
count = 0 

while sandwich_orders and "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    count += 1

if count >= 3:
    print('The deli has run out of pastrami sandwiches.')

while sandwich_orders:
      current_sandwich = sandwich_orders.pop() 
      finished_sandwiches.append(current_sandwich)

print (f'Is there "Pastrami sandwich" in list of finished sandwiches? {"Pastrami sandwich" not in sandwich_orders}')  # will return True if there is no "Pastrami sandwich" in list of finished sandwiches







    

