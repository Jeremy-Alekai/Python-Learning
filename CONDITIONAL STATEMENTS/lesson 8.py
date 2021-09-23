
#LESSON 8 : Comparison Operators 

# Previously, we used the == and != operators to check if two values are equal. 
# When we check for equality, we compare one value to another to determine if they are equal. 
# For this reason, we call == and != comparison operators.

# We can compare value A to value B to determine the following:

#     A is equal to B and vice versa (B is equal to A).
#     A is not equal to B and vice versa.
#     A is greater than B or vice versa.
#     A is greater than or equal to B or vice versa.
#     A is less than B or vice versa.
#     A is less than or equal to B or vice versa.

# In Python, we have special operators for each of the comparison operations above:

# img

# As with == and !=, comparing values using any of the comparison operators above will output a single Boolean value:

# img

# The fact that a comparison outputs a single Boolean value allows us to use a comparison inside an if statement 
# (remember from the second screen that a Boolean value or an expression that evaluates to a Boolean value must 
# follow if):

# img

# These new comparison operators allow us to answer more advanced questions about our dataset:

#     How many apps have a rating of 4.0 or greater?
#     What is the average rating of the apps that have a price greater than $9?
#     How many apps have a price greater than $9?
#     How many apps have a price smaller than or equal to $9?

# Using what we know, we can answer the first question in at least two ways.

apps_4_or_greater = []

for row in apps_data[1:]:

    rating = float(row[7])

    if rating >= 4.0:

        apps_4_or_greater.append(rating)


print(len(apps_4_or_greater))



# Output
# 4781

# Above, we did the following:

#     Initialized an empty list named apps_4_or_greater.
#     Looped through apps_data[1:], and for every iteration, we:
#         Stored the rating value as a float to a variable named rating.
#         Appended the rating to apps_4_or_greater if the value stored in rating was greater than or equal to 4.0.
#     Measured the length of the apps_4_or_greater list to find out the number of apps that have a rating of 4.0 or 
#       greater.
#         After the loop, the apps_4_or_greater list will only store the ratings of the apps that were rated 4.0 or 
#           better. The list apps_4_or_greater has 4,781 ratings that are 4.0 or greater, which means that there 
#           are 4,781 apps that have a rating of 4.0 or greater.

# We can also use another approach to answer the question: 
#   we initialize a variable with a value of 0 and then increment that variable by 1 each time we find a 
#   rating of 4.0 or greater:

# img

# Above, we did the following:

#     Initialized a variable n_of_apps with a value of 0.
#     Looped through apps_data[1:], and for every iteration, we did the following:
#         Stored the rating value as a float to a variable named rating.
#         Incremented the value of n_of_apps by 1 if the value stored in rating was greater than or equal to 4.0.
#     Printed the value of n_of_apps to determine the number of apps with a rating of 4.0 or greater.
#         n_of_apps was incremented by 1 during the loop every time a rating was 4.0 or greater. 
#           The value of n_of_apps is 4,781 after the looping, which means that 4,781 ratings are 4.0 or greater. 
#           Each rating belongs to an app, so this means that there are 4,781 apps that have a rating of 4.0 or 
#           greater.

# Now let's answer the other three questions:

#     What is the average rating of the apps that have a price greater than $9?
#     How many apps have a price greater than $9?
#     How many apps have a price less than or equal to $9?

# INSTRUCTIONS

#     Compute the average rating of the apps that have a price greater than $9.
#         Using a for loop, isolate the ratings of all the apps that have a price greater than $9. 
#           When you iterate over apps_data, don't include the header row.
#         Find the average value of these ratings and assign the result to a variable named avg_rating.

#     Determine how many apps have a price greater than $9 and assign the result to a variable named n_apps_more_9. 
#       You can use the list of ratings from the previous question to find the answer.

#     Determine how many apps have a price less than or equal to $9, and assign the result to a variable named 
#       n_apps_less_9. The list of ratings from the first question can help you find a quick answer.



# ANSWERS

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_greater_or_equal = []
n_apps_more_9 = 0
n_apps_less_9 = 0

for rows in apps_data[1:]:
    ratings = float(rows[7])
    price = float(rows[4]) 
    # app_price = float
    if price >= 9:
        apps_greater_or_equal.append(ratings)
    
    if price >9:
        n_apps_more_9 += 1
        
    if price <= 9:
        n_apps_less_9 += 1
        
avg_rating = sum(apps_greater_or_equal) / len(apps_greater_or_equal)

# below is one of the methods of how you concatenate/combine a string to a non string 
# variable through converting the non-variable into a string.
print('the average user rating is ' +str(avg_rating))

print('apps greater or equal to : ' +str( len(apps_greater_or_equal)))
print('apps greater than 9 : '+str(n_apps_more_9))
print('apps less than or equal to 9 : '+str(n_apps_less_9))


