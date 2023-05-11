# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

def sortString(str):
    l =str.split(',')
    l.sort() 
    new_str = ''
    for word in l:
        new_str += f'{word},'
    print (new_str[:len(new_str) - 1])  #get rid of the last comma
sortString("without,hello,bag,world")









  