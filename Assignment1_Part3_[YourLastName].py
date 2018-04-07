# Use string slicing to print out each word of the following string
# "Geographic Information Systems" one word at a time.

# Name: [your name here!]
# Date: 
# Assignment 1 Part 3
# This script uses string slicing to print out different words in a string.

myString = 'Geographic Information Systems'
         #  0123456789 11       21 23   30

# use slicing to print just the first word
print(myString[0:10])

# use slicing to print just the second word
print(myString[11:22])

# use slicing to print just the third word
print(myString[23:30])

# BONUS: use slicing to print the entire string backwards
print(myString[-7:-1]+ myString[-1]+ myString[-20:-7]+ myString[-31:-20])