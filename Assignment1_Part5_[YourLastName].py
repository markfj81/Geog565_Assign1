# Be sure you have gone through Exercises 2 and 5 including the challenge exercises
# from the textbook before attempting this part.

# This exercise is to get you familiarized with ModelBuilder and ArcGIS and how
# we can use Python to modify and enhance our workflows. You will find the data you need for this
# part in the Data folder that came with the assignment.
# Using this data, use Model Builder to build a model that does the following:

# 1. Defines the projection for each dataset to WA State Plane North FIPS 4601.
# 2. Clips the roads and trees datasets based on the UDistrict boundary
# Then, convert your model to a Python script called UDistrict.py.
# Inspect the code that is automatically generated and try to understand what it produces.

# Modify the generated script and do the following:
# Create a list of files (feature classes) needed (e.g., myList = ["fc1", "fc2", "fc3"])
# Use a loop to define projection of each file (for loop)
# Use a loop to clip the streets and trees using the UDistrict boundary (for or while loop)

# Name: [your name here!]
# Date: 
# Assignment 1 Part 5
# This script is a modified output of Model Builder that projects and clips data in the University District

# your code here
import arcpy

arcpy.env.workspace=''

clip_shape=r'path'
clip_shapes=[[1,2],[3,4],[]]
for item in map:
       clip_shapes.append([item, r'c:\'+str(item)+'.shp'])
       
for item in clip_shapes:
       arcpy.clip_analysis(item[0], clip_feature, 'path', xy_tolerance)
       