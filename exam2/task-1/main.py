# Filter and Calculate Average Age of Adult Users
# Objective: Write a function `calculate_average_age_of_adults` that takes an array of user objects and returns
# the average age of all adult users as a numeric value. Only users who are 18 years or older are considered adults.
# Details:
# - The function should filter out users who are under 18 years old.
# - The function should compute the average of the 'age' values for the remaining adult user objects.
# - The result should be rounded to two decimal places if necessary.

class NoAdultsError(Exception):
    """Exception raised when there are no adults in the list """
    pass

def calculate_average_age_of_adults(users):


    # 1. Filter users who are under 18 years old
    adults = [user for user in users if user['age'] >= 18]

    # If there are no adults, raise an error
    if not adults:
        raise NoAdultsError("There are no adult users ")

    # 2. Calculate the average age for adults
    total_age = sum(user['age'] for user in adults)
    average_age = total_age / len(adults)

    # 3. The average age rounded to two decimal places
    return round(average_age, 2)

# Example user data
users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]


# Testing the function
try:
    print(calculate_average_age_of_adults(users))  # This should print the average age of adult users (18+)
except NoAdultsError as e:
    print(e)