
# QUESTION 2

# It turns out your enthusiasm for weightlifting isn't just for show. You actually have some real talent. 
# In the most recent local competition (the North California Open in the 81KG class), 
# you won your weight class out of four other competitors with a 130 KG snatch.

# INSTRUCTIONS
# Calculate the average snatch score (i.e., third element of each row) for this competition. 
# Store the result in avg_snatch. 
# Based on the average snatch score (i.e., your answer for question 1), was your snatch performance greater than 
# or equal to it? Assign 'Yes' to better_than_average_snatch if that was the case and assign 'No' 
# if otherwise.


# ANSWER

first_place = ["You", "USA", 130, 160, 290]
second_place = ["Jimmy Brown", "USA", 127, 161, 288]
third_place = ["John Smith", "USA", 120, 167, 287]
fourth_place = ["Timothy Bradley", "USA", 140, 140, 280]
fifth_place = ["Malik Brown", "USA", 100, 172, 272]

weight_data =[first_place,second_place,third_place,fourth_place,fifth_place] 

snatch_sum = 0

for weight_lifter in weight_data:
    snatch_score = weight_lifter[-1]
    snatch_sum += snatch_score
    
avg_snatch = snatch_sum/len(weight_data)

my_snatch_score = weight_data[0][-1]

print(avg_snatch)

print(my_snatch_score)

yes = 'better than average snatch'
No = 'Equal to average snatch'

if my_snatch_score > avg_snatch:
    
    print(yes)
    
else:
    print(No)
