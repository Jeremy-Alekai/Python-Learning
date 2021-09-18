# We've just received multiple discounts:

#     5% discount for Lenovo laptops.
#     10% discount for HP laptops.
#     15% discount for Asus laptops.

# Let's compute the discounted prices and determine which is the cheapest laptop!
# instructions

# Updated price variables are available on this screen.

#     Compute the discounted prices for each laptop, and assign them back to the respective variables.
#     Round the price variables to the nearest integer, and then assign them back to the respective variables.
#     Print each updated variable on a new line.


# answers
l_price_discount = int(lenovo_price * 0.5) 
hp_price_discount = int(hp_price * 0.1)
asus_price_discount = int(asus_price * 0.15)

lenovo_price = lenovo_price - l_price_discount
hp_price = hp_price - hp_price_discount
asus_price = asus_price - asus_price_discount
print(lenovo_price)
print(hp_price)
print(asus_price)
