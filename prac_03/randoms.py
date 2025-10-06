import random

print(random.randint(5, 20))  # line 1
#What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
#The result is an integer between 5 and 20, with each run yielding a different random integer.
# Minimum: 5, Maximum: 20.

print(random.randrange(3, 10, 2))  # line 2
#The result of this operation is a random integer belonging to the set {3, 5, 7, 9}.
#Minimum: 3, Maximum: 9.

print(random.uniform(2.5, 5.5))  # line 3
#The result is a float point number between 2.5 and 5.5
#Minimum: 2.5, Maximum: 5.5.

print(random.randint(1, 100))
