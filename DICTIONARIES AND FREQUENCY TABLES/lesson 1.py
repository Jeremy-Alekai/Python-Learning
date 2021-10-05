# Welcome to Python for Data Science: Fundamentals Part II!

# To complete this course you'll need to be comfortable with the basics of programming in Python, 
# covered in Python for Data Science: Fundamentals Part I. Here are a few takeaways you can expect in this course:

#     How to build frequency tables using dictionaries
#     How to create and use functions to speed up our workflow
#     How to install Jupyter Notebook locally
#     How to run code in Jupyter Notebook
#     How to build a portfolio project

# In this lesson on dictionaries and frequency tables, we'll learn how to create and update dictionary values,
#  add new key-value pairs, check for dictionary membership, and count values using dictionaries.

# We'll work with a dataset that stores information for 7,197 mobile apps. Within this dataset, 
# the cont_rating column offers information about the content rating of each app. 
# The content rating of an app (also known as the maturity rating) represents the age required to use that app. 
# The table below shows the unique content ratings in our data set,along with the number of apps specific to each rating:
# 
# Content rating 	Number of apps
            #4+ 	4,433
            # 9+ 	987
            # 12+ 	1,155
            # 17+ 	622

# From the table above, we can see the following:

#     Most apps (4,433) have a content rating of 4+ (only people aged four or older are allowed to use these apps).
#     Apps with a content rating of 17+ are the fewest (622).
#     In the middle, we have the 9+ and 12+ apps — 987 apps have a content rating of 9+, and 1,155 apps have a 
#       rating of 12+.

# If we want to save the data from the table above, we can use two lists — or maybe a list of lists. 
# We'll try this in the following exercise, while on the next screen we'll learn about dictionaries and 
# explore a more efficient solution for storing the data above.
# 
# INSTRUCTIONS

# (The dataset is available under the csv tab in the editor to the right.)

#     Store the data in the table above using two different lists.
#         Assign the list ['4+', '9+', '12+', '17+'] to a variable named content_ratings.
#         Assign the list [4433, 987, 1155, 622] to a variable named numbers.

#     Store the data in the table above using a list of lists. 
#       Assign the list [['4+', '9+', '12+', '17+'], [4433, 987, 1155, 622]] to a variable named content_rating_numbers.

# ANSWER
# two separate lists
content_ratings = [ '4+', '9+', '12+', '17+']

numbers = [ 4433, 987, 1155, 622]

# list of lists
content_rating_numbers = [content_ratings,numbers]

print(content_rating_numbers)



