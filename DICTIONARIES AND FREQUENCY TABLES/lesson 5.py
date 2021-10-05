# # LESSON 5
# The index of a dictionary value is called a key. In '4+': 4433, the dictionary key is '4+', 
# and the dictionary value is 4433. As a whole, '4+': 4433 is a key-value pair.

# img

# Dictionary values can be of any data type: strings, integers, floats, Booleans, lists, and even dictionaries.

d_1 = {'key_1': 'value_1', 

       'key_2': 1,

       'key_3': 1.832,

       'key_4': False,

       'key_5': [1,2,3],

       'key_6': {'inner_key' : 10}
       }

print(d_1)

print(d_1['key_1'])

print(d_1['key_6'])

# Output

{'key_1': 'value_1', 'key_2': 1, 'key_3': 1.832, 

 'key_4': False, 'key_5': [1, 2, 3], 

 'key_6': {'inner_key': 10}}

value_1

{'inner_key': 10}

# Dictionary keys can be almost any data type, except lists and dictionaries.
#  If we use lists or dictionaries as dictionary keys, we'll get an error:

# img

# When we populate a dictionary, Python tries to convert each dictionary key to an integer 
# (even if the key is a data type other than an integer). Python does the conversion using the hash() command:

# img

# For reasons we'll be able to understand later, the hash() command doesn't transform lists and dictionaries to integers.
# It returns an error instead. Notice the error messages are the same as when we tried to use lists or 
#   dictionaries as keys.

print(hash([1,2,3]))

# Output

# TypeError: unhashable type: 'list'

print(hash({'key': 'value'}))

# Output

# TypeError: unhashable type: 'dict'

# When we populate a dictionary, we also need to make sure each key in that dictionary is unique. 
# If we use an identical key for two or more different values, Python keeps only the first key and 
# the last value and removes the others — this means that we'll lose data. We illustrate this below:

# d_1 = {'a_key': 1,

#        'another_key': 2,

#        'a_key': 3,

#        'yet_another_key': 4,

#        'a_key': 5}

print(d_1)

# Output

{'a_key': 5, 'another_key': 2, 'yet_another_key': 4}

# An odd "gotcha" is when we mix integers with Booleans as dictionary keys. 
# The hash() command converts the Boolean True to 1, and the Boolean False to 0. 
# This means the Booleans True and False will conflict with the integers 0 and 1. 
# The dictionary keys won't be unique anymore, and Python will only keep the first key and the last value in cases 
#   like that.

d_1 = {1: 'one', True: 'Boolean'}

d_2 = {False: 'Bool', 0: 'zero'}

d_3 = {0: 'zero', 1: 'one',  2: 'two', True: 'true', False: 'false'}

print(d_1)

print(d_2)

print(d_3)

# Output

{1: 'Boolean'}

{False: 'zero'}

{0: 'false', 1: 'true', 2: 'two'}

# INSTRUCTIONS

#     Create the following dictionary and assign it to a variable named d_1:

{'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

# 2.Examine the code below and determine if it will cause an error. If you think it will cause an error, 
# then assign the Boolean True to a variable named error, otherwise assign False.

{4: 'four',
1.5: 'one point five',
'string_key': 'string_value',
True: 'True',
[1,2,3]: 'a list',
{10: 'ten'}: 'a dictionary'}


# ANSWER

d_1 = { 'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

error = True #because we can't use dictionaries or lists as keys

print(d_1)


