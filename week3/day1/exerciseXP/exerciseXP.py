# 🌟 Exercise 1: Cats
# Instructions
# Using this class
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Barsik", 1)   
cat2 = Cat("Scotch", 4)     
cat3 = Cat("Anfisa", 3)  

def find_oldest(cats):
    max_age = -1
    for cat in cats:
        if cat.age > max_age:
            oldest_cat = cat
            max_age = oldest_cat.age
    return oldest_cat
        
cats = [ cat1, cat2, cat3]
print(f'The oldest cat is {find_oldest(cats).name} and his age is {find_oldest(cats).age}')  

# And what if we have multiple cats with the same maximum age in the list and we want to return all of them?  I will modify my function to return a list of the oldest cats.

cat4 = Cat("Pusik", 4) 
cats = [cat1, cat2, cat3, cat4]

def find_all_oldest_cats(cats):
    oldest_cats = []
    max_age = -1
    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cats = [cat.name]
        elif cat.age == max_age:
            oldest_cats.append(cat.name)
    return oldest_cats        
    
find_all_oldest_cats(cats)
print(f'The oldest cats are {",".join(find_all_oldest_cats(cats))}') 


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print('{} goes woof!'.format(self.name))

    def jump(self):
        print('{} jumps {} cm high!'.format(self.name, self.height *2))

davids_dog = Dog('Rex', 50)
print (f'David has a dog. His dog’s name is {davids_dog.name} and his height is {davids_dog.height}cm.')
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup',20)
print (f'Sarah has a dog. Her dog’s name is {sarahs_dog.name} and his height is {sarahs_dog.height}cm.')
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f'David\'s dog is bigger than sarah\'s dog and his heigh is {davids_dog.height}cm.')
elif sarahs_dog.height > davids_dog.height:
    print(f'Sarah\'s dog is bigger than David\'s dog and his heigh is {sarahs_dog.height}cm.')


# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

def sing_me_a_song(self):
    for element in self.lyrics:
        print(element)

notimetodie= Song(["I should've known","I'd leave alone", "Just goes to show", "That the blood you bleed"])        
sing_me_a_song(notimetodie)

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)
 
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(", ".join(self.animals))   

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print ('We dont have this animal in our zoo.')

    def sort_animals(self):
        sorted_animals = {}
        first_letters = []
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        return sorted_animals   

ramat_gan_safari = Zoo('Ramat Gan Safari')   
ramat_gan_safari.add_animal('zebra')  
ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('tiger')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.add_animal('panda')
ramat_gan_safari.add_animal('koala')
ramat_gan_safari.add_animal('mouse') 
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('zebra')
print(ramat_gan_safari.sort_animals())





        
                            



    






          
