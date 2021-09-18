
# Imagine that we want to buy a new laptop for our machine learning projects. 
# After days of searching, we've come up with a shortlist of three laptops:
#     Lenovo: $1699.99
#     HP: $1799.99
#     Asus: $1899.99

# Let's use the skills we've acquired to perform manipulations with different data types.
# instructions
#     Assign the name of each laptop to three variables named lenovo, hp, and asus, as they are written in the list above.
#     Assign their prices as float numbers to three variables named lenovo_price, hp_price, asus_price.
#     Print each variable in a new line.

#answer

laptop1= "lenovo"
laptop2 = "HP"
laptop3 =  "Asus"

#prices
lenovo_price= 1699.99
hp_price = 1799.99
asus_price = 1899.99

full_collon = ":" 
dollar = "$" 

l_price_str = str(lenovo_price)
hp_price_str = str(hp_price)
asus_price_str = str(asus_price)

print(laptop1 +full_collon +dollar + l_price_str )
print(laptop2 +full_collon +dollar + hp_price_str )
print(laptop3 +full_collon +dollar + asus_price_str)