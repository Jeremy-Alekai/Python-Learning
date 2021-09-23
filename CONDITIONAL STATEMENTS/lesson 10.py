# LESSON 10 - The elif Clause 
# # 

# Let's do some more specific labeling than just "free" and "non-free." 
# We want to label the apps using this convention:

# price 	label
# price == 0 	free
# 0 < price < 20 	affordable
# 20 ≤ price < 50 	expensive
# price ≥ 50 	very expensive

# Using what we know, we can only do the transformations above using a combination of if statements. 
# This is what the process looks like on the small dataset below:

# img

# When an app is free, price == 0.0 evaluates to True and app.append('free') executes. 
# But then the computer continues to do redundant operations — it checks for the following:

#     price > 0 and price < 20
#     price >= 20 and price < 50
#     price >= 50

# We already know the three conditions above will evaluate to False once we determine that price == 0.0 is True. 
# To stop the computer from doing redundant operations, we can use elif clauses:

# img

# The code within the body of an elif clause executes only under the following circumstances:

#     The preceding if statement (or the other preceding elif clauses) resolves to False; and
#     The condition specified after the elif keyword evaluates to True.

# In our case above, if price == 0.0 is True, the computer executes app.append('free') and moves forward 
# without executing any of the following elif clauses.

# If price > 0.0 and price < 20 is True, then app.append('affordable') executes, and the 
# remaining two elif clauses are disregarded. If price >= 20 and price < 50 is True, 
# then app.append('expensive') executes, and the last elif clause is disregarded.

# It's possible to replace the final elif clause with an else clause. 
# For our data above, the output would be identical:

# img

# Note, however, that the logic is different when we use an else clause.
#  For elif price >= 50, app.append('very expensive') will execute only if the price is greater than or equal to 50.
#  For else, there's no condition to meet (other than the previous if and elif clauses resolving to False), 
# and app.append('very expensive') will execute even if the price has a value of -5 or -100.

# img

# Just like else, we must combine the elif clause with a preceding if statement:

# img

#Now, let's iterate through our data set and label each app as "free," "affordable," "expensive," or "very expensive."

# INSTRUCTIONS

# Complete the code in the editor to label each app as "free," "affordable," "expensive," or "very expensive." 
#     Inside the loop, do the following:
#     If the price of the app is 0, label the app as "free" by appending the string 'free' to the 
#       current iteration variable.
#     If the price of the app is greater than 0 and less than 20, label the app as "affordable". 
#       For efficiency purposes, use an elif clause.
#     If the price of the app is greater or equal to 20 and less than 50, label the app as "expensive".
#        For efficiency purposes, use an elif clause.
#     If the price of the app is greater or equal to 50, label the app as "very expensive". 
#       For efficiency purposes, use an elif clause.

# Name the newly created column "price_label" by appending the string 'price_label' to the first row of the 
#   apps_data data set.

# Inspect the header row and the first five rows to see some of the changes you made.

# ANSWERS

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:

    price = float(app[4])

    # Complete code from here
    if price == 0:
        app.append('free')

    elif price > 0 and price < 20 :
        app.append('affordable')

    elif price >= 20 and price < 50:
        app.append('expensive')

    elif price >= 50:
        app.append('very expensive')
        
apps_data[0].append('price_label')

print(apps_data[:6])