import timeit

class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt', 'r') as file:
            self.word_list = set(file.read().splitlines())

    
    # all validations will be later in anagrams.py get_user_input

    # def is_valid_word(self, word):
    #     if not isinstance(word, str):
    #         return False
    #     if not word.isalpha():
    #         return False
    #     return True

    #and for now it will be like this
    def is_valid_word(self, word):
        return word.upper() in self.word_list
    

    # I am not doing here any validation because now after i did main method  in anagrams.py i know that this function will never be called with invalid input. 
    def is_anagram(self, word1, word2):
            return sorted(word1) == sorted(word2) 
    
    # the same issue with validations, I know that this method will be called only with valid input so i will change it a little bit 
    # def get_anagrams(self, word):
    #     if not self.is_valid_word(word):
    #         return []
    #     else:
    #         word = word.upper()
    #         anagrams = []
    #         for w in self.word_list:
    #             if len(word) == len(w):
    #                 if self.is_anagram(word, w):
    #                     anagrams.append(w)
    #         return anagrams

    def get_anagrams(self, word):
        word = word.upper()
        anagrams = []
        for w in self.word_list:
            if len(word) == len(w):
                if self.is_anagram(word, w):
                    anagrams.append(w)
        return anagrams


# anagram = AnagramChecker()
# word = 'meat'
# code_snippet = '''
# anagrams = anagram.get_anagrams(word)
# '''
# anagrams = anagram.get_anagrams(word)
# execution_time = timeit.timeit(stmt=code_snippet, globals=globals(), number=1)
# print(f"Execution time: {execution_time} seconds") # Execution time: 0.01 
# print(anagram.get_anagrams(word))
