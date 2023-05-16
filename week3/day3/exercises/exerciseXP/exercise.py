# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

class Program:
    """
    This program demonstrates the usage of built-in Python functions: abs(), int(), and input().

    It prompts the user for input, performs certain operations using the built-in functions, and prints the results.

    Instructions:
    1. Enter a number to find its absolute value using the abs() function.
    2. Enter a floating-point number to convert it to an integer using the int() function.
    3. Enter your name to display it using the input() function.

    Examples:
    - Input: -5
      Output: The absolute value of -10 is 10

    - Input: 3.5
      Output: The integer value of 3.5 is 3

    - Input: Marina
      Output: Your name is: Marina
    """

    def run(self):
        """
        Executes the program and performs the necessary operations.

        It prompts the user for input, applies the corresponding built-in functions,
        and displays the results on the console.
        """

        # Prompt the user for input
        user_input = input("Enter a number: ") 
        # Convert the user input to a float and calculate the absolute value
        absolute_value = abs(float(user_input))
        print("Absolute value:", absolute_value)


        # Prompt the user for a floating-point number
        float_number = float(input("Enter a floating-point number: "))
        # Convert the floating-point number to an integer
        integer_number = int(float_number)
        print(f"The integer value of {float_number} is {integer_number}")


        # Prompt the user for their name
        user_input = input("Enter your name: ")
        print(f"Your name is: {user_input}")


# Create an instance of the Program class and run the program
program = Program()
program.run()


# 🌟 Exercise 2: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    def __repr__(self):
      return f"{self.amount}{self.currency}s"
    
    def __int__(self):
       return int(self.amount)
    
    def __str__(self):
      return f"{self.amount} {self.currency}s"
    
    def __add__(self, other):
        if isinstance(other, int):
            total_amount = self.amount + other
            return total_amount
        elif isinstance(other, Currency) and self.currency == other.currency:
            total_amount = self.amount + other.amount
            return total_amount
        else:
            raise ValueError("Invalid operand for addition assignment.")
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
            return self
        else:
            raise ValueError("Invalid operand for addition assignment.")
    
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
# '5 dollars'

print(int(c1))
# 5

print(c1)
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>



