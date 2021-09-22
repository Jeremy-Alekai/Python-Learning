# QUESTION 3
# Beware of the data types of each row in weightlifting_81kg.

# INSTRUCTIONS
#  Without using for loops, what was the average snatch score for the top five performers (stored in top_5) 
#   at the world championships? Store this value as average_snatch_top_5 and print it.

# ANSWER
from csv import reader 

open_file = open('weightlifting.csv')

read_file = reader(open_file)

weightlifting_81kg = list(read_file)

header = weightlifting_81kg[0]

weightlifting_81kg = weightlifting_81kg[1:]

top_5 = weightlifting_81kg[:5]

first = float(weightlifting_81kg[0][-1])
second = float(weightlifting_81kg[1][-1])
third = float(weightlifting_81kg[2][-1])
fourth = float(weightlifting_81kg[3][-1])
fifth = float(weightlifting_81kg[4][-1])

snatch_sum = first + second + third + fourth + fifth

average_snatch_top_5 = snatch_sum/len(weightlifting_81kg[:5])
print(snatch_sum) 
