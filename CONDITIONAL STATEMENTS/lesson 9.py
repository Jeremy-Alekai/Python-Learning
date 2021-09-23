
# # LESSON 9 : The else Clause

# Let's use information from the price column to label each app as "free" or "non-free." 
# If the price equals 0.0, we want to label the app "free." Otherwise, we want to label it "non-free."

# Remember that we store our data set as a list of lists — each row is a list that describes an app. 
# To label the app, we want to add the string 'free' or 'non-free' at the end of each list (row). 
# On a smaller scale, this is what we want to do (below, we're using just a small extract from our data set, 
# showing just the name and the price of four apps):

# img

# In the code above, we iterated through the apps_data list of lists, and for each iteration, we did the following:

#     We saved the price value to a variable named price.
#     If price == 0.0, we appended the string 'free' to the list app (app is the iteration variable).
#     If price != 0.0, we appended the string 'non-free' to the list app.

# For each iteration, the computer checked whether price == 0.0 and price != 0.0. 
# But once we know that price == 0.0 for an app, we don't need to also check price != 0.0 for the same app.

# In our small dataset above, we have three free apps. 
# The computer evaluated price == 0.0 as True three times, and then it checked ifr price != 0.0 for the same number
#  of times. This means that the computer performed three redundant operations 
# — it still evaluated price != 0.0 while knowing that price == 0.0 is True.

# If we have a dataset with 5,000 free apps, this would mean 5,000 redundant operations. 
# We can avoid this redundancy by combining an if statement with an else clause:

# img

# The code within the body of an else clause executes only if the if statement that precedes it resolves to False.

# img

# Here's an example that's similar to our example above:

# img

# In our example above (the example at the beginning of this screen), the code within the body of the else clause 
# executes only if price == 0.0 evaluates to False. If price == 0.0 is True,
#  then the code app.append('free') executes, and the computer moves forward without executing the else clause.

# Note that we must combine an else clause with a preceding if statement. 
# We can have an if statement without an else clause, but we can't have an else clause without a preceding if statement.

# img

# When we combine a statement with a clause, we create a compound statement — 
# combining an if statement with an else clause makes up a compound statement.

# INSTRUCTIONS

#     Complete the code in the editor to label each app as "free" or "non-free" depending on its price.
#         Inside the for loop, do the following:
#             If the price of the app is 0.0, then label the app as "free" by appending 
#               the string 'free' to the current iteration variable.
#             Else, label the app "non-free" by appending the string 'non-free' to the current iteration variable. 
#               Don't 'non_free' for 'non-free'.
#         By adding labels to the end of each row, we basically created a new column. 
#           Name this column "free_or_not" by appending the string 'free_or_not' to the first row of the apps_data 
#           data set. Do this outside the for loop.

#     Print the header row and the first five rows to see some of the changes we made.

# ANSWERS

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    
    if price == 0.0:
        app.append('free')
    else :
        app.append('non-free')
                         
apps_data[0].append('free_or_not')
print(apps_data[:6])
print(len(apps_data[:6]))
