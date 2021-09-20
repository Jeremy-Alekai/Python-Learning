# LESSON 6
# Previously, we introduced lists as a better alternative than using one variable per data point. 
# Instead of having a separate variable for each of the five data points 'Facebook', 0.0, 'USD', 2974676, 3.5, 
# we can bundle the data points together into a list and then store the list in a single variable.
# So far, we've been working with a dataset containing five rows, and we've been storing each row as a list in 
# a separate variable (the variables row_1, row_2, row_3, row_4, and row_5). 
# If we had a data set with 5,000 rows, however, we'd end up with 5,000 variables, which will make our code almost 
# impossible to work with.

# To solve this problem, we can store our five variables in a single list:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]

row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]

row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

data_set = [row_1, row_2, row_3, row_4, row_5]

print(data_set)

# Output
 
# Notice the double brackets at the beginning
[['Facebook', 0.0, 'USD', 2974676, 3.5], 

 ['Instagram', 0.0, 'USD', 2161558, 4.5], # Notice the commas

 ['Clash of Clans', 0.0, 'USD', 2130805, 4.5], 

 ['Temple Run', 0.0, 'USD', 1724546, 4.5], 

 ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]]

# As we can see, data_set is a list that stores five other lists (row_1, row_2, row_3, row_4, and row_5).
# A list that contains other lists is called a list of lists.

# The data_set variable is still a list, which means we can retrieve individual list elements and perform list slicing 
# using the syntax we learned. Below, we'll do the following:

#     Retrieve the first list element (row_1) using data_set[0]
#     Retrieve the last list element (row_5) using data_set[-1]
#     Retrieve the first two list elements (row_1 and row_2) by performing list slicing using data_set[:2]

# img

# We'll often need to retrieve individual elements from a list that's part of a list of lists — for instance, 
# we may want to retrieve the value 3.5 from ['Facebook', 0.0, 'USD', 2974676, 3.5], which is part of the 
# data_set list of lists. Below, we extract 3.5 from data_set using what we've learned:

#     We retrieve row_1 using data_set[0], and assign the result to a variable named fb_row.
#     We print fb_row, which outputs ['Facebook', 0.0, 'USD', 2974676, 3.5].
#     We retrieve the last element from fb_row using fb_row[-1] (since fb_row is a list), and we assign the result to a variable named fb_rating.
#     We print fb_rating, which outputs 3.5

# img

# Above, we retrieved 3.5 in two steps: we first retrieved data_set[0], and then we retrieved fb_row[-1]. However, there's an easier way to retrieve the same value of 3.5 by chaining the two indices ([0] and [-1]) — the code data_set[0][-1] retrieves 3.5:

# img

# Above, we've seen two ways of retrieving the value 3.5. 
# Both ways lead to the same output (3.5), but the second way involves less typing because it combines 
# the steps we see in the first case. While you can choose either option, people generally choose the second one.

# INSTRUCTIONS

# In the code editor, we've already stored the five rows as lists in separate variables.
#Group the five lists together in a list of lists. Assign the resulting list of lists to a variable named app_data_set.
# Compute the average rating of the apps by retrieving the right data points from the app_data_set list of lists.
# The rating is the last element of each row. You'll need to add up the ratings and then divide by the number of ratings.
# Assign the result to a variable named avg_rating.

# ANSWER

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1]+app_data_set[1][-1]+app_data_set[2][-1]+ app_data_set[3][-1]+ app_data_set[4][-1])/5
print(avg_rating)
