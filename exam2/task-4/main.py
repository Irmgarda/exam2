# Add Suffix
# Objective: Write a function `add_suffix` that returns a lambda expression. This lambda expression
# should transform its input by adding a specified suffix at the end.
# Parameters:
# - suffix: A string representing the suffix to be added to the input.
# Returns:
# - A lambda function that takes a string input and appends the specified suffix to it.

def add_suffix(suffix):
    return lambda word: word + suffix # - A lambda function that takes a string input and appends the specified suffix to it.

add_ment = add_suffix("ment") # A lambda function that takes a string input and appends the specified suffix to it.
add_able = add_suffix("able") #should transform its input by adding a specified suffix at the end.

# Examples:


print(add_able("remark"))  # Expected: "remarkable"
print(add_able("break"))   # Expected: "breakable"




print(add_ment("enjoy"))   # Expected: "enjoyment"
print(add_ment("develop")) # Expected: "development"
