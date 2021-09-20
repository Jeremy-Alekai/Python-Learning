# Often, we need to retrieve more than one element from a list. 
# Let's say we have the list ['Facebook', 0.0, 'USD', 2974676, 3.5], and we're interested in isolating only the 
# name of the app and the data about ratings (the number of ratings and the rating). 
# This is how we can do that:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

app_name = row_1[0]

n_of_ratings = row_1[3]

rating = row_1[-1]

# If we want to do this for every app, we'll get a lot of variables, making our code lengthy and hard to navigate. 
# A better solution is to store the data we want in a separate list.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]

print(fb_rating_data)

#Output

#['Facebook', 2974676, 3.5]

# Above, we managed to isolate the three list elements of interest in a separate list. 
# To do that, we used the code row_1[0], row_1[3], row_1[-1] to retrieve the first, fourth, and last element, 
# and then we surrounded that part of code with square brackets to create a new list.


# INSTRUCTIONS
    # For Facebook, Instagram, and Pandora — Music & Radio, isolate the rating data in separate lists. Each list should contain the name of the app, the rating count, and the user rating. Don't forget that indexing starts at 0.
    #     For Facebook, assign the list to a variable named fb_rating_data.
    #     For Instagram, assign the list to a variable named insta_rating_data.
    #     For Pandora — Music & Radio, assign the list to a variable named pandora_rating_data.

    # Compute the average user rating for Facebook, Instagram, and Pandora — Music & Radio using the data you stored in fb_rating_data, insta_rating_data, and pandora_rating_data.
    #     You'll need to add the ratings together first, and then divide the total by the number of ratings.
    #     Assign the result to a variable named avg_rating.
    #     As a side note, we could calculate the average rating here a little bit better using the weighted mean.

# ANSWER
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0],row_1[-2],row_1[-1]]
insta_rating_data = [row_2[0],row_2[-2],row_2[-1]]
pandora_rating_data = [row_5[0],row_5[-2],row_5[-1]]

total = row_1[-1]+row_2[-1]+row_5[-1]

avg_rating = total/3
                  
