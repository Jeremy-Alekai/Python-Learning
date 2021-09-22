# LESSON 2

# On the previous screen, we used if price == 0.0 to check whether price equals 0.0. 
# When we use the == operator to determine if two values are equal, the output we get will always be True or False:

# img

# Although they may look like strings, True and False belong to a different data type:

print(type(True))

# Output

# <class 'bool'>

print(type(False))

# Output

# <class 'bool'>

# We call True and False Boolean values or Booleans — we can see in the code example above that their data type is 
# bool ("bool" is an abbreviation for "Boolean").

# Boolean values (True and False) are necessary parts of any if statement. 
# One of the following must always follow if:

#     a Boolean value
#     an expression that evaluates to a Boolean value

# img

# We should indent the code in the body of an if statement four spaces to the right 
# (technically, we only need to indent the code one space to the right, but the convention in the Python community is
#  to use four spaces per indentation level — this is an important habit to form in case you will one day collaborate
#  with others).

# img

# The indented code only executes when True follows if. 
# When False follows if, the code inside the body doesn't execute. 
# Notice in the diagram below that '1 - Output' and '3 - Output' are printed, while '2 - Output' isn't.

# img

# Note that we can have more than one line of code in the body of an if statement. 
# Below, we see three lines of code for each if statement.

# img

# INSTRUCTIONS

# In the code editor, we've already initialized the variable a_price with a value of 0. 
# Transcribe the following sentences into code using if statements:

#     If a_price equals 0, then print the string 'This is free' (remember to use the == operator for equality).
#     If a_price equals 1, then print the string 'This is not free'.


# ANSWERS

a_price = 0

if a_price == 0:
    print('This is free')
    
if a_price == 1:
    print('This is not free')