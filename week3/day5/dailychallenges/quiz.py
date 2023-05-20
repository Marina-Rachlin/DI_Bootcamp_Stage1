import random

# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# A class is a blueprint or prototype for creating objects 

# What is an instance?
# An instance is an object that belongs to a class.

# What is encapsulation?
# Encapsulation is a concept of bundling data and methods within a single unit.

# What is abstraction?
# Abstraction it is a process of handling complexity by hiding unnecessary information (internal details) from the user and showing only the functionality.

# What is inheritance?
# Inheritance is a mechanism in which one class acquires the property of another class.

# What is multiple inheritance?
# Multiple inheritance is a feature of some object-oriented computer programming languages 
# in which an object or class can inherit characteristics and features from more than one parent object or parent class.

# What is polymorphism?
#  Polymorphism is a concept that refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

# What is method resolution order or MRO?
# MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.




# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for value in values:
                self.cards.append((suit, value))

    def shuffle(self):
        if len(self.cards) > 52:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            card = random.choice(self.cards)
            self.cards.remove(card)
            return card
        else:
            return None
        
# deck = Deck()
# print(len(deck.cards))
# print(deck.deal())
# print(len(deck.cards))
# deck.shuffle()
# print(deck.deal())
# print(len(deck.cards))



