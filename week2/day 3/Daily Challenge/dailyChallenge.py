# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = 'froggy'
dict_letters = dict()

for char in word:
    ind = [i for i, a in enumerate(word) if a == char]
    if char not in dict_letters:
        dict_letters[char] = ind
print (dict_letters) 

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$13"
res_list = list()

items_purchase = {key: int(val[1:]) for key, val in items_purchase.items()}
for key, value in items_purchase.items():
     if value <= int(wallet[1:]):
        res_list.append(key)

if len(res_list) > 0: # checking if the list is not empty
    res_list.sort() # sorting in alphabetical order.
    print(res_list)
else:
    print('Nothing') # if the list is empty

