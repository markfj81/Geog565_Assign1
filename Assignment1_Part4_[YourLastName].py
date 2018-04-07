# Instructions:
# Create a script that determines if a list of integers contains duplicates.
# If it does contain duplicates, print out "This list contains duplicates".
# If the list does NOT contain duplicates, print out the smallest number in the list.
# Use the following lists for testing: [2, 8, 64, -16, 32, 4, 16, 8, -30] and [2, 8, 64, -16, 32, 4, 16, 18, -30]


# Name: [Mark Johnson]
# Date:4/5/2018
# Assignment 1 Part 4
# This script determines if a list of integers contains duplicates.

list1 = [2, 8, 64, -16, 32, 4, 16, 8, -30]
list2 = [2, 8, 64, -16, 32, 4, 16, 18, -30]

# your code here
print ("List1: ") 
if len(list1) != len(set(list1)):
    print ("This list contains duplicates")
else:
    print (min(list1))
    
print ("\nList2: ")   
if len(list2) != len(set(list2)):
    print ("This list contains duplicates")
else:
    print (min(list2))