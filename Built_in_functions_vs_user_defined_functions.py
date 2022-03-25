tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Create a variable for the max_price and call the max() function and populate the function with the given variables
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)

# Doing the same thing as previously but to work out the minimum price
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)

# Using the round function to round to one decimal places
#help(round)
rounded_price = round(tshirt_price, 1)

# Printing commands
print(max_price)
print("")
print(min_price)
print("")
print(rounded_price)
print("")