# 





# ANSWERS
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings)/len(games_social_ratings)

print(avg_games_social)