# Now we'll learn an alternative method for computing the average rating value. 
# Once we create a list, we can add (or append) values to it using the append() command.

# img

# Unlike other commands we've learned, append() has a special syntactical usage, 
# following the pattern list_name.append() rather than simply append() 
# (we'll examine this syntactical quirk once we learn about functions and methods).

# Now that we know how to append values to a list, we can take the following steps to compute the average app rating:

#     We initialize an empty list.
#     We start looping over our data set and extract the ratings.
#     We append the ratings to the empty list we created in step one.

# Once we have all the ratings, we do the following:
#    Use the sum() command to add all the ratings (to be able to use sum(), we'll need to store the ratings as floats 
#     or integers)
#    Divide the sum by the number of ratings (which we can get using the len() command).

# Below, we can see these steps for our dataset containing five rows:

# img

# INSTRUCTIONS

# Using the new technique we've learned, compute the average app rating for all of the 7,197 apps stored in our dataset.

#     Initialize an empty list named all_ratings.
#     Loop through the apps_data[1:] list of lists (don't include the header row). 
# For each of the 7,197 iterations of the loop, do the following:
#         Extract the rating of the app and store it to a variable named rating (the rating has the index number 7). 
#           Convert the rating value from a string to a float.
#         Append the value stored in rating to the list all_ratings.
#     Compute the sum of all ratings using the sum() command.
#     Divide the sum of all ratings by the number of ratings, and assign the result to a variable named avg_rating.
#     Print the results of avg_rating.

# ANSWERS

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

all_ratings = []

for app_rating in apps_data[1:]:
    rating = float(app_rating[7])
    all_ratings.append(rating)
    
# print(all_ratings)

avg_rating = sum(all_ratings)/len(all_ratings)
print(avg_rating)