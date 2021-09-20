# The dataset we've been working with so far is an extract from a much larger dataset:
# 	id 	track_name 	size_bytes 	currency 	price 	rating_count_tot 	rating_count_ver 	user_rating 	user_rating_ver 	ver 	cont_rating 	prime_genre 	sup_devices.num 	ipadSc_urls.num 	lang.num 	vpp_lic
# 0 	24882215 	Facebook 	389879808 	USD 	0.00 	2974676 	212 	3.5 	3.5 	95.0 	4+ 	Social Networking 	37 	1 	29 	1
# 1 	389801252 	Instagram 	113954816 	USD 	0.00 	2161558 	1289 	4.5 	4.0 	10.23 	12+ 	Photo & Video 	37 	0 	29 	1
# 2 	529479190 	Clash of Clans 	116476928 	USD 	0.00 	2130805 	579 	4.5 	4.5 	9.24.12 	9+ 	Games 	38 	5 	18 	1
# 
# Data source: Mobile App Store data set (Ramanathan Perumal)

# Our best strategy so far has been to type each data point and bundle them efficiently into a list of lists. 
# The data set above, however, has 7,197 rows and 16 columns, which amounts to 115,152 (7,197 ×

# 16) data points — typing all that would take us days. We'd also be bound to make typing errors, 
# which will eventually lead to wrong data and false conclusions. Fortunately, we can leverage Python to store 
# this data set as a list of lists in a matter of seconds.

# A dataset is generally stored as a file in a computer — the data set above is stored as a file named AppleStore.csv. 
# we start by opening the file using the open() command:

opened_file = open('AppleStore.csv')

print(opened_file)

# ​

# Output

# <_io.TextIOWrapper name='AppleStore.csv' mode='r' encoding='UTF-8'>

# open('AppleStore.csv') returned the output <_io.TextIOWrapper name='AppleStore.csv' mode='r' encoding='UTF-8'>. 
# The output is an object. For now, all we have to keep in mind is that the AppleStore.csv file will open once open('AppleStore.csv') has finished running.

# Once we've opened the file, we read it in using a command called reader(). 
# We import the reader() command from the csv module using the code from csv import reader 
# (a module is a collection of commands and variables.

opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)

print(read_file)

# Output
# <_csv.reader object at 0x7f55b0a379e0>

# Just like open('AppleStore.csv'), reader(opened_file) returned an object. Now that we've read the file, we can transform it into a list of lists using the list() command:

opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)

apps_data = list(read_file)

# The apps_data variable above is a list of lists, and it stores a dataset of 7,197 rows and 16 columns. Below, we print only the first five rows of apps_data by using list slicing (we colored the output of each list differently to help you read the output more easily):

# img

# Although there are 7,197 rows (apps) in our dataset, len(apps_data) indicates there are 7,198 rows because it also considers the header row, which describes the column names (the first row).

opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)

apps_data = list(read_file)

print(len(apps_data))

# Output

# 7198

# As a side note, the AppleStore.csv file is currently located on our servers. 
# Later on in this course, we'll help you set up your own environment locally — you'll be able to run Python code 
# and open the AppleStore.csv on your own local computer (you're currently running code and opening the file in a 
# browser).




# INSTRUCTIONS
# Open the AppleStore.csv file and store it as a list of lists.
# Open the file using the open() command. Save the output to a variable named opened_file.
# Read in the opened file using the reader() command (we've already imported reader() for you from the csv module). Save the output to a variable named read_file.
# Transform the read-in file to a list of lists using the list() command. Save the list of lists to a variable named apps_data.
# Explore apps_data. You could do the following:
# Print its length using the len() command
# Print the first row (the row describing column names)
# Print the second and the third row (try to use list slicing here)

#ANSWER
opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)

apps_data = list(read_file)

print(len(apps_data))

print(apps_data[0])

print(apps_data[1:3])

