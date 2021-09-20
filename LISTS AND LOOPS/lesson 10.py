
# Now we'll move on to computing the average rating for the data set that has 7,197 rows. 
# Remember, first we need to open the file AppleStore.csv and transform it into a list of lists:

# img

# If we use the technique we learned and loop over apps_data to get the rating sum, we'll get a TypeError:

# img

# This error happens because the first row of apps_data doesn't contain numbers (it describes column names). 
# In the loop body, we assign the value of row[7] to the rating variable, and then we add rating to rating_sum.
#  But for the first iteration of the loop, row[7] takes the string value 'user_rating' (which is a column name).
#  This means that running rating_sum + rating is equivalent to 0 + 'user_rating', which causes a TypeError because 
# we can't add strings and integers.

# Theoretically, we have two solutions:

# We remove the first row from apps_data, and then we start the iteration over. 
# We do that by doing the following:
#         Saving the header row to a separate variable named header
#         Saving apps_data[1:] back to apps_data — apps_data[1:] is a list slice that excludes the first row 
#           (the header row)
#     We iterate directly over apps_data[1:], which is a list slice that excludes the first row.

# img

# We got the same error. Upon inspection of some of the rows in apps_data, we see that quotation marks surround 
# all the values, which suggests they are strings. Once again, the error is a result of trying to add a string to 
# an integer.

print(apps_data[1])

print(apps_data[1][7])

print(type(apps_data[1][7]))

# Output

# ['284882215', 'Facebook', '389879808', 'USD', '0.0', 

#  '2974676', '212', '3.5', '3.5', '95.0', '4+', 

#  'Social Networking', '37', '1', '29', '1']

# 3.5

# <class 'str'>

# We need to convert strings to integers or floats (decimal numbers) using the int() and float() commands. 
# The ratings are expressed as decimal points, so we'll convert them to floats using the float() command.

# img 


# INSTRUCTIONS

# Compute the average app rating for all the 7,197 apps stored in the data set.

# Initialize a variable named rating_sum with a value of zero.
# Loop through the apps_data[1:] list of lists (make sure you don't include the header row). 
# For each of the 7,197 iterations of the loop (for each row in apps_data[1:]) do the following:
# Extract the rating of the app and store it to a variable named rating (the rating has the index number 7). 
# Convert the rating value from a string to a float using the float() command.
# Add the value stored in rating to the current value of the rating_sum.
# Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. 
# Store the result in a variable named avg_rating.

# ANSWER
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for each_row in apps_data[1:]:
    rating = float(each_row[7])
    rating_sum +=rating
    avg_rating =rating_sum/7197 
    
print(rating_sum)
print(avg_rating)
    
