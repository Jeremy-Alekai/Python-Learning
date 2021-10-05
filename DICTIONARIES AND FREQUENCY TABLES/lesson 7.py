# # LESSON 7 - Counting with Dictionaries

# Once we've created and populated a dictionary, we can update (change) the dictionary values. 
# To update a dictionary value, we need to reference it by its corresponding dictionary key and then perform 
# the updating operation we want. In the code example below, we do the following:

#     Change the value corresponding to the dictionary key '4+' from 4433 to 0.
#     Add 13 to the value corresponding to the dictionary key '9+'.
#     Subtract 1155 from the value corresponding to the dictionary key '12+'.
#     Change the value corresponding to the dictionary key '17+' from 622 (integer) to '622' (string).

# img

# We can combine updating dictionary values with what we already know to count how many times each unique content 
# rating occurs in our data set. 
#  Let's start by considering the list ['4+', '4+', '4+', '9+', '9+', '12+', '17+'], which stores a few content ratings. 
# 
# To use code to count how many times each rating occurs in this short list, we could do the following:

#     Create a dictionary where the keys are the unique content ratings and the values are all 0:
#            {'4+': 0, '9+': 0, '12+': 0, '17+': 0}.

#     Loop through the list ['4+', '4+', '4+', '9+', '9+', '12+', '17+'], and for each iteration, do the following:

#         Check if the iteration variable exists as a key in the previously created dictionary.
#         If it exists, then increment the dictionary value at that key by 1.

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

for c_rating in ratings:

    if c_rating in content_ratings:

        content_ratings[c_rating] += 1

print(content_ratings)

# Output

{'4+': 3, '9+': 2, '12+': 1, '17+': 1}

# To get a better understanding of how this works, we'll print the content_rating dictionary inside the for-loop 
# to see how it changes with every iteration, do the following:

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

for c_rating in ratings:

    if c_rating in content_ratings:

        content_ratings[c_rating] += 1

    print(content_ratings)

print('Final dictionary:')

print(content_ratings)

# Output

{'4+': 1, '9+': 0, '12+': 0, '17+': 0}

{'4+': 2, '9+': 0, '12+': 0, '17+': 0}

{'4+': 3, '9+': 0, '12+': 0, '17+': 0}

{'4+': 3, '9+': 1, '12+': 0, '17+': 0}

{'4+': 3, '9+': 2, '12+': 0, '17+': 0}

{'4+': 3, '9+': 2, '12+': 1, '17+': 0}

{'4+': 3, '9+': 2, '12+': 1, '17+': 1}

# Final dictionary:

{'4+': 3, '9+': 2, '12+': 1, '17+': 1}

# Now let's read in our AppleStore.csv data set, and use the technique above to count the number of times each 
# unique content rating occurs. We should arrive at the same numbers we've been using in the table:
# 
# Content rating 	Number of apps
            # 4+ 	4,433
            # 9+ 	987
            # 12+ 	1,155
            # 17+ 	622
# 
# INSTRUCTIONS

#     Count the number of times each unique content rating occurs in the data set.
#         Create a dictionary named content_ratings where the keys are the unique content ratings and 
#           the values are all 0 (the values of 0 are temporary at this point, and they'll be updated).
#         Loop through the apps_data list of lists. Make sure you don't include the header row. 
#               For each iteration of the loop, do the following:
#             Assign the content rating value to a variable named c_rating. 
#               The content rating is at index number 10 in each row.
#             Check if c_rating exists as a key in content_ratings. 
#           If it exists, then increment the dictionary value at that key by 1 
#               (the key is equivalent to the value stored in c_rating).
#         Outside the loop, print content_ratings to check if the counting worked as expected.

# ANSWERS
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
        
print(content_ratings)