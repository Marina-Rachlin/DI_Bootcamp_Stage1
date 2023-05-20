from  anagram_checker import AnagramChecker
import timeit

def get_user_input():
    while True:
        user_input = input("Enter a word or type 'q' to quit: ").strip().lower()
        if user_input == 'q':
            return None
        elif len(user_input.split()) > 1:
            print("Error: Only a single word is allowed.")
        elif not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
        else:
            return user_input

def display_word_info(word, is_valid, anagrams):
    print(f"YOUR WORD: {word}")
    if is_valid:
        print("This is a valid English word.")
        print("Anagrams for your word:", ", ".join(anagrams))
    else:
        print("This is not a valid English word.")

def main():
    checker = AnagramChecker()

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        word = get_user_input()

        if word == None:
            break

        is_valid = checker.is_valid_word(word)
        anagrams = checker.get_anagrams(word)
        display_word_info(word, is_valid, anagrams)


code_snippet = '''
anagrams = main()
'''
execution_time = timeit.timeit(stmt=code_snippet, globals=globals(), number=1)
print(f"Execution time: {execution_time} seconds")