# Who Passed the Course?
# Objective: Write a function `who_passed` that takes a dictionary of student names and a list of their test scores over the semester,
# and returns a list of all the students who passed the course. A student passes if they scored 100% on all tests.
# The list should be returned in alphabetical order.
# Parameters:
# - students: A dictionary where the keys are student names (strings) and the values are lists of test scores (strings in the format "x/y").
# Returns:
# - A list of student names who passed the course, sorted in alphabetical order.
# Notes:
# - All test scores must be 100% for the student to pass.
# - Return the list of names in alphabetical order.

def who_passed(students):
 passed_students = [] #Initialize a list of passed students:

 for student, scores in students.items(): #iterate to students scores
   if all(int(score.split('/')[0]) == int(score.split('/')[1]) for score in scores): # Check if score at least 100%
     passed_students.append(student) # add the passed student
     return sorted(passed_students) # return the list of passed students

# Examples:
print(who_passed({
  "John" : ["5/5", "50/50", "10/10", "10/10"],
  "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
  "Adam" : ["8/10", "22/25", "3/5", "5/5"],
  "Barry" : ["3/3", "20/20"]
}))  # Expected: ["Barry", "John"]

print(who_passed({
  "Zara" : ["10/10"],
  "Kris" : ["30/30"],
  "Charlie" : ["100/100"],
  "Alex" : ["1/1"]
}))  # Expected: ["Alex", "Charlie", "Kris", "Zara"]

print(who_passed({
  "Zach" : ["10/10", "2/4"],
  "Fred" : ["7/9", "2/3"]
}))  # Expected: []