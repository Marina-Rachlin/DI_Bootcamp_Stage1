import random
import json

# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

def get_words_from_file():
    words = []  # Use a list to store the words
    with open('sowpods.txt', "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            words.append(line.strip())
    return words

# print(get_words_from_file())

def get_random_sentence(length):
    words = get_words_from_file()  
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words)
    return sentence.lower()

# print(get_random_sentence(5))
# print(get_random_sentence(3))


def main():
    print("Welcome to random sentence generator! This program generates a random sentence based on the length you specify.")
    
    user_input = input("Enter the length of the sentence (between 2 and 20): ")
    try:
        length = int(user_input)
        if length < 2 or length > 20:
            raise ValueError
        sentence = get_random_sentence(length)
        print("Random Sentence:", sentence)
    except ValueError:
            print("Invalid input.")

main()

# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.

data = json.loads(sampleJson) # parse the JSON string
salary = data["company"]["employee"]["payable"]["salary"]
print(salary)


# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
data = json.loads(sampleJson)
data["company"]["employee"]["birth_date"] = "1992-01-07"
updatedJson = json.dumps(data, indent = 4)
print (updatedJson)

# Save the dictionary as JSON to a file.

file_path = "new_file.json" # specify the file path
with open(file_path, "w") as file: # open the file in write mode
    json.dump(data, file)   # write the dictionary as JSON to the file
print("JSON data saved to file:", file_path)

# explained each step for myself in order to better remember :)