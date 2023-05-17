from collections import Counter
import string

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


class Text():
    def __init__(self, text):
        self.text = text

    def get_word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency > 0:
            return frequency
        else:
            return f"The word '{word}' is not found in the text."
        
    def get_most_common_word(self):
        words = self.text.split()
        word_counts = Counter(words)
        most_common_word, frequency = word_counts.most_common(1)[0]
        return most_common_word    
    
    def get_unique_words(self):
        words = self.text.split()  
        unique_words = set(words)  
        return list(unique_words)
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


# text = Text("A good book would sometimes cost as much as a good house.")
# print(text.get_word_frequency('good'))
# text = Text("A good book would sometimes cost as much as a good house.")
# print(text.get_most_common_word())
# print(text.get_unique_words())


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.

# Now, use the provided the_stranger.txt file and try using the class you created above.

# Look above...

print(Text.from_file('the_stranger.txt').get_most_common_word())
print(Text.from_file('the_stranger.txt').get_unique_words())
print(Text.from_file('the_stranger.txt').get_word_frequency('day'))


# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        return self.text.translate(str.maketrans('', '', string.punctuation))
    
    def remove_stop_words(self):
        with open('stop_words_english.txt', 'r') as file:
            stop_words = [word.strip() for word in file.readlines()]
        words = self.text.split()
        words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
        return ' '.join(words)
    
    def remove_special_characters(self):
        cleaned_text = ''.join(char for char in self.text if char.isalnum() or char.isspace())
        return cleaned_text
    
print (TextModification.from_file('the_stranger.txt').remove_punctuation())   
print (TextModification.from_file('the_stranger.txt').remove_stop_words())  
print (TextModification.from_file('the_stranger.txt').remove_special_characters()) 


