# 5. Multiple Conditions

# So far, we've only worked with single conditions, like the following:

#     If price equals 0.0 (if price == 0)
#     If genre equals "Games" (if genre == 'Games')

# Single conditions won't allow us to answer more advanced questions, like these:

#     What's the average rating of free gaming apps?
#     What's the average rating of non-free gaming apps?
#     What's the average rating of free non-gaming apps?
#     What's the average rating of non-free non-gaming apps?

# Fortunately, we can combine two or more conditions together into a single if statement using the and keyword. 
# In the two diagrams below, we can use and to simultaneously check whether an app is both free and has a gaming genre.

# img

# Notice above that code like app1_price == 0 and app1_genre == 'Games' outputs a single Boolean value.

# img

# Python evaluates any combination of Booleans to a single Boolean value:

# img

# As a general rule, when we combine Booleans using and, the resulting Boolean is True only if all the Booleans are 
# True. If any of the Booleans are False, then the resulting Boolean will be False:

# img

# Let's now use multiple conditions to determine the average rating of free gaming apps.

# INSTRUCTIONS

# Complete the code in the editor to compute the average rating of free gaming apps.
#     Inside the for loop, append the rating to the free_games_ratings list if the price equals 0.0 and 
#       the genre equals 'Games'.
#     Outside the for loop, compute the average rating of free gaming apps. 
#       Assign the result to a variable named avg_rating_free_games.
# 

# ANSWER
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
        # Complete code from here

    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
        

    
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

print(avg_rating_free_games)
