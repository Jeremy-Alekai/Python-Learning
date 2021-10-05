
# # LESSON 4

# In order to create a dictionary, we need to do the following:

#     Map each index to its corresponding value by following an index:value pattern (e.g. '4+': 4433).
#     Type the entire sequence of index:value pairs, and separate each pair with a comma 
#       (e.g. '4+': 4433, '9+': 987, '12+': 1155, '17+': 622).
#     Surround the sequence with curly braces (e.g. {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}).

# img

# Alternatively, we can create a dictionary and populate it with values by following these steps:

#     Create an empty dictionary.
#     Add values one by one to that empty dictionary.

# Adding a value to a dictionary follows the pattern dictionary_name[index] = value. 
# To add a value 4433 with an index '4+' to a dictionary named content_ratings, 
#   we need to use the code content_ratings['4+'] = 4433.

content_ratings = {} 

content_ratings['4+'] = 4433

print(content_ratings)

# Output

{'4+': 4433}

# We can keep adding values using the same approach:

content_ratings = {} 

content_ratings['4+'] = 4433

content_ratings['9+'] = 987

content_ratings['12+'] = 1155

content_ratings['17+'] = 622

print(content_ratings)

# Output

{'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# This approach is the same as populating an empty list by using the list_name.append() command.
#  The syntax is different, but fundamentally we take the same steps:

#   Create an empty dictionary (or list).
#   Add values using the dictionary_name[index] = value technique (or the list_name.append() command in case of a list).

# In the next exercise, we'll focus on practicing this new technique.

# INSTRUCTIONS

#     Use the new technique we learned to map content ratings to their corresponding numbers inside a dictionary.
#         Create an empty dictionary named content_ratings.
#         Add the index:value pairs one by one using the dictionary_name[index] = value technique. 
#           This should be the final form of the dictionary: {'12+': 1155, '17+': 622, '4+': 4433, '9+': 987}.

#     Retrieve the value at index 12+ from the content_ratings dictionary. 
#       Assign it to a variable named over_12_n_apps.


# ANSWERS

content_ratings = {}

content_ratings['12+'] = 1155
content_ratings['17+'] = 622
content_ratings['4+'] = 4433
content_ratings['9+'] = 987

over_12_n_apps = content_ratings['12+']

print(over_12_n_apps)
