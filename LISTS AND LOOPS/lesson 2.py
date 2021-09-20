
# lesson 2

# A list can contain both mixed and identical data types. A list like [4, 5, 6] has identical data types (only integers),
# while the list ['Facebook', 0.0, 'USD', 2974676, 3.5] has mixed data types:

#     Two strings ('Facebook', 'USD')
#     Two floats (0.0, 3.5)
#     One integer (2974676)

# The ['Facebook', 0.0, 'USD', 2974676, 3.5] list has five data points. 
# To find the length of a list, we can use the len() command:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

print(len(row_1))

list_1 = [1, 6, 0]

print(len(list_1))

list_2 = []

print(len(list_2))

#Output

# 5

# 3

# 0

# For small lists, we can just count the data points on our screens to find the length, 
# but the len() command will prove very useful later when we work with lists containing thousands of elements 
# (we'll see an actual example later in this lesson).
# Each element (data point) in a list has a specific number associated with it — this is an index number. 
# The indexing always starts at 0, so the first element will have the index number 0, the second element will have the
#  index number 1, and so on.
# To quickly find the index of a list element, identify its position in the list, and then subtract 1
# For example, the string 'USD' is the third element of the list (position number 3), so its index number must be 2 
# since 3−1=2

# The index numbers help us retrieve individual elements from a list. 
# Looking back at the list row_1 from the code example above, we can retrieve the first element (the string 'Facebook') 
# with the index number 0 by running the code print(row_1[0]).

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

print(row_1[0])

# ​Output

# Facebook

# The syntax for retrieving individual list elements follows the model list_name[index_number]. 
# For instance, the name of our list above is row_1, and the index number of the first element is 0 — following 
# the list_name[index_number] model, we get row_1[0], where the index number 0 is in square brackets after the variable 
# name row_1.
# Retrieving list elements makes it easier to perform operations. 
# For instance, we can select the ratings for Facebook and Instagram and find the average or the difference between 
# the two:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]

difference = row_2[4] - row_1[4]

average_rating = (row_1[4] + row_2[4]) / 2

print(difference)

print(average_rating)

# Output
# 1.0
# 4.0

# INSTRUCTIONS
# In the code editor, you can already see the lists for the first three rows.

# The fourth element in each list describes the number of ratings an app has received. 
# Retrieve the fourth element from each list, and then find the average value of the retrieved numbers.
#     Assign the fourth element from the list row_1 to a variable named ratings_1. 
#     Don't forget that the indexing starts at 0.
#     Assign the fourth element from the list row_2 to a variable named ratings_2.
#     Assign the fourth element from the list row_3 to a variable named ratings_3.
#     Add the three numbers retrieved together and save the sum to a variable named total.
#     Divide the sum (now saved in the variable total) by 3 to get the average number of ratings for the first three rows. 
# Assign the result to a variable named average.

# ANSWER
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

ratings_1 =  row_1[3]
ratings_2 =  row_2[3]
ratings_3 =  row_3[3]

total = row_1[3]+row_2[3]+row_3[3]
average = total/3
