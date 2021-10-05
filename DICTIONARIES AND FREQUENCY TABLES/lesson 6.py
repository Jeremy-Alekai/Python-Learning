# # LESSON 6

# Previously, we worked with a small table showing the four unique content ratings in our data set, 
# along with the number of apps corresponding to each rating.

# Content rating 	Number of apps
# 4+ 	4,433
# 9+ 	987
# 12+ 	1,155
# 17+ 	622

# You might have wondered how we managed to count the number of apps for each unique content rating. 
# How did we find out there are 4,433 apps with a 4+ content rating, or 622 apps with a 17+ rating? 
# Part of the answer is a technique that uses the special properties of dictionaries. 
# The full answer is a bit lengthier: we'll learn how to count the number of apps for each unique content rating on 
# the next two screens.

# Once we've created a dictionary, we can check if a certain value exists in the dictionary as a key. 
# We can check, for instance, if the value '12+' exists as a key in the dictionary 
#       {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}. 
# 
# To do that, we use the in operator.

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print('12+' in content_ratings)

# Output

True

# The '12+' in content_ratings expression returned the Boolean True. 
# This is because the string '12+' exists in the dictionary content_ratings as a key.

# If we use in with a certain value that doesn't exist among a dictionary's keys, we'll get False. 
# For instance, checking if the string '10+' exists in the dictionary content_ratings returns False because 
# there's no dictionary key '10+' in content_ratings.

# content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print('10+' in content_ratings)

print('12+' in content_ratings)

# Output
False
True

# Checking if 4433 or 987 exists in content_ratings also returns False because the search is only for the 
# dictionary's keys (4433 and 987 exist as dictionary values in content_ratings).

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(4433 in content_ratings)

print(987 in content_ratings)

# Output

False
False

# An expression of the form a_value in a_dictionary always returns a Boolean value:

#     We get True if a_value exists in a_dictionary as a dictionary key.
#     We get False if a_value doesn't exist in a_dictionary as a dictionary key.

# Now let's practice using the in operator.

# INSTRUCTIONS

# Using the in operator, check whether the following values exist as dictionary keys in the content_ratings dictionary:

#         The string '9+'. Assign the output of the expression to a variable named is_in_dictionary_1.
#         The integer 987. Assign the output of the expression to a variable named is_in_dictionary_2.

# Combine the output of an expression containing in with an if statement. If the string '17+' exists as dictionary key 
# in content_ratings, then do the following:
#         Assign the string "It exists" to a variable named result.
#         Print the result variable.


# ANSWER

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = "It exists"
    print(result)

# Alternative solution
is_in_dictionary = '17+' in content_ratings
if is_in_dictionary:
    result = "It exists"
    print(result)