# There are several ways to format strings. Please read section 4.12 of the
# textbook for more information. In this part of the assignment, please use
# the three different string formatting methods to print out the following
# string: 'A string is a sequence of characters'. Use the methods in whatever way you see fit.

# Name: [Mark Johnson]
# Date: 4/3/2018
# Assignment 1 Part 2
# This script demonstrates the three different ways to format strings.

string = 'A string is a sequence of characters'
int = 5
strA = 'A string'
strB = 'is a'
strC = 'sequence of'
strD = 'characters'
strFormat = '{} is a {} characters{}'
# method 1: the comma
print 'Method 1:', strA, strB,  int

# method 2: the + sign concatenator
print ('\nMethod 2: ' + strA +' ' + strB + ' ' + strC + ' ' + strD)

# method 3: the format method
print ('\nMethod 3: ' + strFormat.format(strA, 'sequence of','!' ))
       
       
       
       
      