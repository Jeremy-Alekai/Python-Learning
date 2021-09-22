# QUESTION 1

# You're a huge weightlifting enthusiast, and every year, you tune in to the annual weightlifing world championships.
# This year, you're pumped to watch your idol, Lu Xiaojun, maintain his supremacy in the 81KG class, 
# and you decided to collect some info about the competitor's performance in this particular class for analysis.

# INSTRUCTIONS
#     Using the dataset provided, weightlifting.csv, 
#       open and read in the dataset into a list of lists called weightlifting_81kg.
#     Store the first row (which contains the name of the columns) as header.
#         Store the rest of the information as weightlifting_81kg.

# ANSWER
open_file = open('weightlifting.csv')

from csv import reader
read_file = reader(open_file)
weightlifting_data = list(read_file)

weightlifting_81kg = []

header = weightlifting_data[1:]
for all_data in header:
    weightlifting_81kg.append(all_data)