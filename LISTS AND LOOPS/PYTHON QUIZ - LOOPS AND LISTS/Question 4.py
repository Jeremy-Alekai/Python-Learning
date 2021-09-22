
#QUESTION 4 
# All right, the top five appear to be quite far from you. That's fine. 
# Just being at the World Championships would still be a pretty cool achievement. 
# Let's see how you would fare against the entire group of competitors on the world stage. 

# INSTRUCTIONS
# Utilizing for loops, do the following:

#     Calculate the average snatch score of all competitors in the 81KG class. 
#       Store this value as average_snatch_world, and print it.

#     Create a list containing the difference between the competitor's snatch score against 
#       your best performance (your_best_snatch), and store it in a variable called comparison.


# ANSWER    not sure about this answer
from csv import reader 

open_file = open('weightlifting.csv')
read_file = reader(open_file)
weightlifting_81kg = list(read_file)

header = weightlifting_81kg[0]
weightlifting_81kg = weightlifting_81kg[1:]

your_best_snatch = 130

snatch_sum = 0

for competitors in weightlifting_81kg:
    snatch_scores = competitors[-1]
    snatch_sum += float(snatch_scores)
    
average_snatch_world = snatch_sum/len(weightlifting_81kg)

print(average_snatch_world)

comparison = [your_best_snatch,average_snatch_world]
print(comparison)