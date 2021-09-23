# 7. Combining Logical Operators
# 
# In the previous exercise, we computed the average rating of the apps with a genre that is either "Social Networking"
#  or "Games." We can ask even more specific questions, like these:

#     What is the average rating of free apps with a genre that is either "Social Networking" or "Games"?
#     What is the average rating of non-free apps with a genre that is either "Social Networking" or "Games"?

# To answer the first question, we need to isolate the apps that meet the following criteria:

#     Are in either the "Social Networking" or "Games" genre
#     And have a price of 0.0

# To isolate these apps, we can combine or with and in a single if statement:

# img

# Notice that we enclosed the genre == 'Social Networking' or genre == 'Games' part within parentheses. 
# This helps Python understand the specific logic we want for our if statement.

# img

# If we don't use the parentheses, Python defaults to unwanted results — like incorrectly including non-free apps. 
# In the example below, we see that not using parentheses leads us to classifying a non-free app as free.

# img

# Above, we printed 'This gaming or social networking app is free!!' for a non-free app. 
# This is an example of a logical error.

# In the case of a syntax or runtime error, the computer stops the code from running and raises an error.
#  For logical errors, the computer doesn't raise any error — the code runs just fine, and the logical error slips
#  through. To prevent this, we should pay extra attention to the logic of our code.

# Using parentheses correctly makes a difference:

# img

# In the code editor on the right, we added the code we used above to extract the ratings for free gaming or 
# social networking apps. This code should serve as an example for the exercise below.

# INSTRUCTIONS

#     Compute the average rating of non-free apps with a genre that is either "Social Networking" or "Games."
#         Assign the result to a variable named avg_non_free.
#         Try to complete this exercise without any additional guidance. You may feel a bit confused at first, but we've practiced the steps you need to solve this kind of problem several times. Essentially, the code is almost identical to what we used to extract the ratings for free gaming or social networking apps.

# ANSWER

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free_games_social_ratings.append(rating)
        
avg_non_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)

# Non-free apps (average)
print(avg_non_free)