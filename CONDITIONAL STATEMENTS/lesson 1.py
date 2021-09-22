
# LESSON 1

# In this lesson on conditional statements, we'll learn how to ask more advanced questions about datasets, 
# including the following:

#     How to use if, else, and elif statements
#     How to use logical operators
#     How to use comparison operators

# We'll be working with a dataset that stores information for 7,197 mobile apps, 
# and we'll ask questions like the following (in regards to average ratings):

#     What's the average rating of non-free apps?
#     What's the average rating of free apps?

# To answer these two questions, we need to find a way to separate free apps from non-free apps because 
# they are all listed together in our dataset. More specifically, we could do the following:

#     Isolate the ratings for free and non-free apps in separate lists.
#     Compute the average rating for each list.

# Before we isolate the ratings for the free apps, let's look at how to use the list_name.append() command to 
# extract the ratings into a separate list. In the code below, we do the following:

#     Convert the AppleStore.csv file into a list of lists, and assign that list of lists to a variable named apps_data.
#     Create an empty list named ratings.
#     Iterate over apps_data[1:] (which excludes the header row), and for each iteration (row), we do the following:
#         Extract the rating and convert it to a float using float(row[7]). 
#       The rating has the index number 7 and comes as a string, so we need to convert it to a float.
#         We assign the rating to a variable named rating.
#         We append rating to the ratings list we created outside the loop using ratings.append(rating) command.

# img

# The problem with this approach is that it includes all the ratings for both free and non-free apps.
#  To isolate only the ratings of the free apps, we need to add a condition to our code. 
# Specifically, we want to add a rating to the ratings list only if the price equals 0.0:

# img

# To implement the condition above (If the price equals 0.0, then do:) in our code, we can use an if statement:

# img

# In the example above, we iterate over the apps_data[1:], and for each iteration, we do the following:

#     Assign the rating as a float to a variable named rating.
#     Assign the price as a float to a variable named price. 
# (The price also comes as a string, so we need to convert it to a float.)
#     If the price is equals 0.0, we append the rating to the ratings list (if the price is 0.0, 
#   then it means the app must be free). 
#   Whenever price doesn't equal 0.0, the code ratings.append(rating) doesn't execute.

# Here are a few things to notice about the if statement:

#     The if statement starts with if, it continues with price == 0.0, and it ends with :.
#     We use the == operator to check whether price is equal to 0.0. Don't confuse == with = 
#      (= is a variable assignment operator in Python; 
#       we use it to assign values to variables — it doesn't tell us anything about equality).
#     We indent ratings.append(rating) four spaces to the right relative to the if statement.

# On the next screen, we'll explain if statements. But first, let's try an if statement exercise.


# INSTRUCTIONS

# (The AppleStore.csv is available under the csv tab in the editor to the right.)

# Complete the code in the editor to find the average rating for free apps.

#     Inside the for loop, do the following:
#     Assign the price of an app as a float to a variable named price. The price is the fifth element in each row (the index starts at 0).
#     If price == 0.0, append the value stored in rating to the free_apps_ratings list using the list_name.append() command (note the free_apps_ratings is already defined in the code editor). Be careful with indentation.
#     Outside the for loop body, compute the average rating of free apps. Assign the result to a variable named avg_rating_free. The ratings are stored in the free_apps_ratings list.


# ANSWERS
# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price == 0.0:
        free_apps_ratings.append(rating)
    
avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)

print(avg_rating_free)
# print(apps_data[0])

