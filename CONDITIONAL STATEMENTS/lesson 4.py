# 4.The Average Rating of Gaming Apps

# So far, we've used the == and != operators only with integers and floats. 
# But we can use them with other data types as well, such as strings or lists:

# img

# This enables us to answer more nuanced questions about our data set, like the following:

#     What's the average rating for gaming apps?
#     What's the average rating for non-gaming apps?

# Note that the prime_genre column describes the app genre, and the genre of gaming apps is encoded as 'Games':
# 	id 	track_name 	size_bytes 	currency 	price 	rating_count_tot 	rating_count_ver 	user_rating 	user_rating_ver 	ver 	cont_rating 	prime_genre 	sup_devices.num 	ipadSc_urls.num 	lang.num 	vpp_lic
# 0 	284882215 	Facebook 	389879808 	USD 	0.0 	2974676 	212 	3.5 	3.5 	95.0 	4+ 	Social Networking 	37 	1 	29 	1
# 1 	389801252 	Instagram 	113954816 	USD 	0.0 	2161558 	1289 	4.5 	4.0 	10.23 	12+ 	Photo & Video 	37 	0 	29 	1
# 2 	529479190 	Clash of Clans 	116476928 	USD 	0.0 	2130805 	579 	4.5 	4.5 	9.24.12 	9+ 	Games 	38 	5 	18 	1
# 3 	420009108 	Temple Run 	65921024 	USD 	0.0 	1724546 	3842 	4.5 	4.0 	1.6.2 	9+ 	Games 	40 	5 	1 	1
# 4 	284035177 	Pandora - Music & Radio 	130242560 	USD 	0.0 	1126879 	3594 	4.0 	4.5 	8.4.1 	12+ 	Music 	37 	4 	1 	1

# To compute the average rating of gaming apps, we can use the same approach we used on the previous screen 
# when we computed the average rating of free and non-free apps. In the code example below, we do the following:

#     Initialize an empty list named games_ratings.
#     Loop through apps_data[1:], where apps_data is a list of lists that stores our data set. 
#       For each iteration, we do the following:
#         Assign the rating as a float to a variable named rating.
#         Assign the genre to a variable named genre. The genre will be saved as a string.
#         Append the rating value stored in rating to the list games_ratings if the value in genre is equal to 
#           the string 'Games'.
#     Compute the average rating of gaming apps, and assign the result to avg_rating_games.
#     Print avg_rating_games.

# img

# Now let's compute the average rating of non-gaming apps.

# INSTRUCTIONS

# Using the same techniques in the diagram above, compute the average rating of non-gaming apps.

#     Initialize an empty list named non_games_ratings.
#     Loop through the apps_data list of lists (make sure you don't include the header row).
#     For each iteration of the loop, do the following:
#         Assign the rating of the app as a float to a variable named rating 
#           (the index number of the rating column is 7).
#         Assign the genre of the app to a variable named genre (index number 11).
#         If the genre is not equal to 'Games', append the rating to the non_games_ratings list.

#     Compute the average rating of non-gaming apps, and assign the result to a variable named avg_rating_non_games.

#     Optional exercise: compare the average rating of gaming apps (3.69) with the average rating of non-gaming apps. 
#       Why do you think we see this difference?

# ANSWERS

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []

for row in apps_data[1:]:
    rating =float( row[7])
    genre = row[11]
    
    if genre != 'Games':
        non_games_ratings.append(rating)

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

print(avg_rating_non_games)
'''On average, gaming apps have greater ratings compared to non-gaming apps.
This might be because gaming apps offer much more entertainment, which
makes the users more inclined to give higher ratings.'''