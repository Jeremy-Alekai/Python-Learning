# To simplify things, it's better to round the prices to integers because we don't need to worry about cents 
# when the prices are high.

# Let's do it!
# ### instructions

# 1. Updated price variables are available on this screen.
# 2. Round the variables lenovo_price, hp_price, and asus_price to the nearest integer, 
# and then assign them back to the respective variables.
# 3. Print each updated variable in a new line.

#answer
lenovo_price_str = int(lenovo_price)
hp_price_str = int(hp_price)
asus_price_str = int(asus_price)

print(lenovo_price_str)
print(hp_price_str)
print(asus_price_str)