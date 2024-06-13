# Validate price
# Objective: Write a function `has_valid_price` that checks if each product has a valid price. A valid price must be either an integer or a float, and greater than or equal to zero. Products with a price of 0 are considered free and count as valid.
# Parameters:
# - product: A dictionary containing product details with at least a 'price' key.
# Returns:
# - A Boolean value: True if the product has a valid price, False otherwise.
# Details:
# - If the price is not an integer or a float, return False.
# - If the price is less than zero, return False.
# - If the product is None or does not contain a 'price' key, return False.

def has_valid_price(product):
# 1.Ensure the product is a dictionary and contains the 'price' key
    if isinstance(product, dict) and 'price' in product:
        price = product['price']
        # Check if a valid price either an integer or a float, and greater than or equal to zero. Products with a price of 0 are considered free and count as valid
        if isinstance(price, (int, float)) and price >= 0:
            return True
    return False

# Define test dictionaries
product_milk = {"product": "Milk", "price": 1.50} #True if the product has a valid price
product_cheese = {"product": "Cheese", "price": -1} #If the price is less than zero, return False
product_eggs = {"product": "Eggs", "price": 0} # If the price is less  or equal to zero, return False
product_cereals = {"product": "Cereals", "price": "3.0"} # If the price is not an integer or a float, return False
product_none = None #  If the product is None or does not contain a 'price' key, return False
product_no_price = {"product": "Butter"} # If the product is None or does not contain a 'price' key, return False

# Testing the conditions
print(has_valid_price(product_milk))
print(has_valid_price(product_cheese))
print(has_valid_price(product_eggs))
print(has_valid_price(product_cereals))
print(has_valid_price(product_none))
print(has_valid_price(product_no_price))

# Desired Outcome:
# print(has_valid_price({ "product": "Milk", "price": 1.50 }))  # Expected: True
# print(has_valid_price({ "product": "Cheese", "price": -1 }))  # Expected: False
# print(has_valid_price({ "product": "Eggs", "price": 0 }))  # Expected: True
# print(has_valid_price({ "product": "Cereals", "price": "3.0" }))  # Expected: False
# print(has_valid_price(None))  # Expected: False
