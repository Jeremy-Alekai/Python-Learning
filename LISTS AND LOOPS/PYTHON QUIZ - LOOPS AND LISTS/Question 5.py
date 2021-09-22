
# QUESTION 3

# In the U.S., the preferred unit of measure for load is pounds (lbs). 
# So as impressive as your lifts are, no one has any context for how much that really is. 
# So let's convert everything.

# NB: Conversion from pounds to kilograms is multiplying by 0.4536 lbs/kg

# ANSWER

from csv import reader 

open_file = open('weightlifting.csv')
read_file = reader(open_file)
weightlifting_81kg = list(read_file)

header = weightlifting_81kg[0]
weightlifting_81kg = weightlifting_81kg[1:]

conversion_factor = float(0.4536)

for pounds  in weightlifting_81kg:
    snatch_lbs = float(pounds[-1]) *conversion_factor

print(snatch_lbs)