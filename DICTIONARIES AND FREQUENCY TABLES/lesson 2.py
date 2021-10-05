# lesson 2

# On the previous screen, we saw a table that shows the unique content ratings in our dataset,
#  along with the number of apps specific to each rating:

# Content rating 	Number of apps
            # 4+ 	4,433
            # 9+ 	987
            # 12+ 	1,155
            # 17+ 	622

# We stored the data above in two ways:

#     Using two separate lists
#     Using a single list of lists

# img

# Looking at the lists above, it may not be clear which content rating corresponds to which number 
# — especially for someone without enough context. 
# We need to find a better way to map a content rating to its corresponding number.

# Each list element has an index number. Let's consider the numbers list:

# img

# What if we could transform the index numbers to content rating values? 
# This way, the mapping between content ratings and their corresponding numbers would be much clearer.

# img

# Fortunately, we can do this using a dictionary:

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings)

# Output

{'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# To create the dictionary above, we do the following:

#     Map each content rating to its corresponding number by following an index:value pattern. 
#      For instance, to map a rating of '4+' to the number 4,433, 
#       we type '4+': 4433 (notice the colon between '4+' and 4433). To map '9+' to 987, we type '9+': 987, and so on.

#     Type the entire sequence of index:value pairs, and separated each with a comma: 
        #   '4+': 4433, '9+': 987, '12+': 1155, '17+': 622.

#     Surround the sequence with curly braces: {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# The animation below demonstrates the transition from table to dictionary.

# img

# Now, let's try to create the content_ratings dictionary ourselves.

# INSTRUCTIONS

#     Map content ratings to their corresponding numbers by recreating the dictionary above: 
#       {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}. 
#       Assign the dictionary to a variable named content_ratings.
#     Print content_ratings, and examine the output carefully.

# ANSWER

content_ratings = { '4+': 4433, '9+':987, '12+':1155, '17+' : 622}

print(content_ratings)