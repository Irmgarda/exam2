# Class: OnesThreesNines
# Objective: Create a class `OnesThreesNines` that calculates the minimum number of ones, threes, and nines needed to sum up to a given integer.
# The result should be stored in a variable `self.answer
# Parameters:
# - An integer between 0 and 26.
# Returns:
# - A string in the format "nines:x, threes:y, ones:z".
# Notes:
# - Each of the ones, threes or nines could only be either 0, 1 or 2.
# - After the comma, you must put a space.

class OnesThreesNines:
    def __init__(self, num):
        self.num = num
        self.answer = self.calculate_answer()

    def calculate_answer(self):
        nines = self.num // 9 #  how many 9 are into the given number
        remainder = self.num % 9 # mod 9
        threes = remainder // 3 #  how many 3 are into the given number
        ones = remainder % 3 # mod 3
        return f"nines:{nines}, threes:{threes}, ones:{ones}"

# Examples:
otn1 = OnesThreesNines(10)
print(otn1.answer)  # Expected: "nines:1, threes:0, ones:1"

otn2 = OnesThreesNines(15)
print(otn2.answer)  # Expected: "nines:1, threes:2, ones:0"

otn3 = OnesThreesNines(22)
print(otn3.answer)  # Expected: "nines:2, threes:1, ones:1"
