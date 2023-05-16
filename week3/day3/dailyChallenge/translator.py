from translate import Translator

# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator(from_lang="fr", to_lang="en")

def translate(word):
    return translator.translate(word)

result = {word: translate(word) for word in french_words}
print(result)