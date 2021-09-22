# The technique we've just learned is called a loop. 
# Because we always start with for (like in for some_variable in some_list:), we call this technique a for loop.

# These are the structural parts of a for loop:

# img

# The indented code in the body gets executed the same number of times as elements in the iterable variable.
#  If the iterable variable is a list containing three elements, the indented code in the body gets executed 
# three times. We call each code execution an iteration, so there will be three iterations for a list that has 
# three elements. For each iteration, the iteration variable will take a different value, following this pattern:

# For the first iteration, the value is the first element of the iterable (if the iterable is the list [1, 3, 5], 
# then the value will be 1).

# For the second iteration, the value is the second element of the iterable (if the iterable is the list [1, 3, 5],
# then the value will be 3).

# For the third iteration, the value is the third element of the iterable (if the iterable is the list [1, 3, 5], 
# then the value will be 5).

# img

# The code outside the loop body can interact with the code inside the loop body. 
# For instance, in the code below we do the following:

# Initialize a variable a_sum with a value of zero outside the loop body.
# We loop (or iterate) over a_list. For every iteration of the loop, we do the following:
# Perform an addition (inside the loop body) between the current value of the iteration variable value and the current value stored in a_sum (a_sum was defined outside the loop body).
# Assign the result of the addition back to a_sum (inside the loop body).
# Print the value of the a_sum variable (inside the loop body). 
# Notice that the value of a_sum changes after each addition. At the end of the loop, a_sum has the value 9, 
# which is equivalent to the sum of the numbers in a_list (1 + 3 + 5).

# img

# Above, we created a way to add the numbers in a list. We can use this technique to sum the ratings in our data sets. 
# Once we have the sum, we only need to divide by the number of ratings to get the average value. 
# Let's begin by computing the average rating value for the dataset with five rows.


# INSTRUCTIONS

# Compute the average app rating for the apps stored in the app_data_set variable.
# Initialize a variable named rating_sum with a value of zero outside the loop body.
# Loop (iterate) over the app_data_set list of lists. 
# For each of the five iterations of the loop (for each row in app_data_set):
# Extract the rating of the app and store it to a variable named rating. 
# The rating is the last element of each row.
# Add the value stored in rating to the current value of the rating_sum.
# Outside the loop body, divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. 
# Store the result in a variable named avg_rating.

# ANSWER
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for each_row in app_data_set:
    rating = each_row[-1]
    rating_sum  += rating

avg_rating = rating_sum/5
print (rating_sum)
