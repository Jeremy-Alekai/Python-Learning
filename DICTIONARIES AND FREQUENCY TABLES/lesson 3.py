
# # LESSON 3

# Using a dictionary allowed us to change the index numbers of a list to content rating values. 
# That way, the mapping between content ratings and their corresponding numbers became much clearer.

# numbers = [4433, 987, 1155, 622]
# Index num   0     1     2    3

# numbers = [4433, 987, 1155, 622]
# # Index num  0    1     2    3
# #          '4+'  '9+' '12+' '17+' 

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings)

# Output

{'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# To retrieve the individual values of the content_ratings dictionary, we can use the new indices. 
# We retrieve individual dictionary values the same way we retrieve individual list elements 
#       — we follow a variable_name[index] pattern:

numbers = [4433, 987, 1155, 622]

print(numbers[0])

print(numbers[2])

# ​

# Output

4433

1155

# Alternatively, using a dictionary:

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings['4+'])

print(content_ratings['12+'])

# Output

4433

1155

# Now, let's practice retrieving a few dictionary values.

# INSTRUCTIONS

#     Retrieve values from the content_ratings dictionary.
#         Assign the value at index '9+' to a variable named over_9.
#         Assign the value at index '17+' to a variable named over_17.

#     Print over_9 and over_17.

# ANSWERS

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']

over_17 = content_ratings['17+']

print(over_17)

print(over_9)

# OUTPUT
622
987