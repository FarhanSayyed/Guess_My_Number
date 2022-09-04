import random
import math
# Taking Inputs to Define the Range of the Number(Lower)
lower = int(input("Enter Lower Limit:- "))
 
# Taking Inputs to Define the Range of the Number(Upper)
upper = int(input("Enter Upper Limit:- "))
 
'''Generating a Random Number Between
the Lower and Upper Limit'''
generatedNum = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
'''For Calculation of Minimum Number of
Guesses Depends Upon Range'''
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # Considering User's Guess
    guess = int(input("Guess a number:- "))
 
    # Evaluating the Number entered by user
    if generatedNum == guess:
        print("Congratulations you did it in ",
              count, " try")
        # If guessed, loop will break
        break
    elif generatedNum > guess:
        print("Your Number is too small!")
    elif generatedNum < guess:
        print("Your Number is too big!")
 
# If User Fail to Guess the Number in Given Chances, 

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % generatedNum)
    print("\tBetter Luck Next time!")
 