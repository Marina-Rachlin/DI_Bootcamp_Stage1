from exerciseXP import Dog
import random

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


class Petdog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight):
        super().__init__(dog_name, dog_age, dog_weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        text = ""
        for dog in args:
            text += f"{dog.name},"
        print(f"{text[:-1]}all play together.")


    def do_a_trick(self):
        sentences = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        print(f'{self.name} is not trained' if not self.trained else f'{self.name} {random.choice(sentences)}')

dog1 = Petdog('Rex',10, 15)
dog2 = Petdog('Albi', 7, 15)
dog3 = Petdog('Reichel', 9, 16)
pet_dogs = [dog1, dog2, dog3]
for pet in pet_dogs:
    pet.do_a_trick()
    pet.play(dog1, dog2, dog3)
    pet.train()
    pet.do_a_trick()
   
        

    