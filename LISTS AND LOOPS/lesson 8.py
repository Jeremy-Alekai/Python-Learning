# Previously in this lesson, we wanted to compute the average rating of an app. 
# This was a doable task when we were working with only five rows, but our data set now has 7,197 rows.
#  Our best strategy was to do the following:
#     Retrieve each individual rating.
#     Sum the ratings.
#     Divide by the number of ratings.

# EXAMPLE

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]

row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]

row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + 
                app_data_set[4][-1]) / 5

print(avg_rating)

# Output

# 4.2

# Retrieving 7,197 ratings manually is impractical because it would take a very long time. 
# We need to find a way to retrieve all 7,197 ratings in a matter of seconds.

# Looking at the code example above, we see that a process keeps repeating: 
# we select the last list element for each list within app_data_set. 
# The app_data_set stores five lists, so we repeat the same process five times. 
# What if we could tell Python directly that we want to repeat this process for each list in app_data_set?

# Fortunately, we can do that — Python offers us an easy way to repeat a process, which helps us when we need to 
# repeat a process hundreds, thousands, or even millions of times.

# Let's say we have a list [3, 5, 1, 2] assigned to a variable ratings, and we want to repeat the following process: 
# for each element in ratings, print that element. This is how we could translate that into Python syntax:

# img

# In our first example above, the process we want to repeat is "extract the last element for each list in app_data_set".
#  This is how we can translate that process into Python syntax:

# img

# Let's consider what happens above. Python isolates each list element from app_data_set one at a time and assigns it 
# to each_list (which basically becomes a variable that stores a list — we'll discuss this more on the next screen):

# img

# The code in the last diagram above is a simplified version of the code below:

# img

# Using the technique above requires us to write a line of code for every row in the data set. 
# But using the for each_list in app_data_set technique requires us to write only two lines of code regardless of 
# the number of rows in the data set — the data set can have five rows or one million.

# One of our goals is to use this new technique to compute the average rating for our five rows above, 
# and our other goal is to compute the average rating for our data set with 7,197 rows.
#  We'll do exactly that over the next few screens in this lesson, but for now, we'll focus on practicing this 
# technique.

# Before writing any code, we need to indent the code we want repeated four space characters to the right:

# img

# Technically, we only need to indent the code at least one space character to the right, but the convention in 
# the Python community is to use four space characters. This helps with readability — it will be easier for other 
# people who follow this convention to read your code, and it will be easier for you to read theirs.



# INSTRUCTIONS

# Use the new technique we've learned to print all the rows in the app_data_set list of lists.
#     You'll need to translate this pattern into Python syntax: for each list in the app_data_set variable, 
#       print that list.
#     Remember to use indentation.

# ANSWER
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for each_list in app_data_set:
    print(each_list)
