# lesson 3

# In Python, we have two indexing systems for lists:

#  Positive indexing: the first element has the index number 0, the second element has the index number 1, and so on.
#  Negative indexing: the last element has the index number -1, the second to last element has the index number -2, and so on.

# img

# In practice, we almost always use positive indexing to retrieve list elements. Negative indexing is useful when we want to select the last element of a list — especially if the list is long, and we can't tell the length by counting.

# img

# Notice that if we use an index number that is outside the range of the two indexing systems, we'll get an IndexError.
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1[6])

# Output
# IndexError: list index out of range

# INSTRUCTIONS
# The last element in each list shows the average rating of each application.

# Retrieve the ratings for the first three rows, and then find the average value of all the ratings retrieved.
#     Assign the last element from the list row_1 to a variable named rating_1. 
#   Try to take advantage of negative indexing.
#     Assign the last element from the list row_2 to a variable named rating_2.
#     Assign the last element from the list row_3 to a variable named rating_3.
#     Add the three ratings together and save the sum to a variable named total_rating.
#     Divide the total by 3 to get the average rating. Assign the result to a variable named average_rating.

#ANSWER
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[-1]

rating_2 = row_2[-1]

rating_3 = row_3[-1]

total_rating = rating_1 + rating_2 + rating_3

average_rating = total_rating/3


