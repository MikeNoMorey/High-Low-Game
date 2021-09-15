# // Michael Morey // 09/14/21 // Pseudo-Code //

# IMPORT: (RANDOM) LIBRARY
#
# OUTPUT: 'Welcome to the Higher/Lower game Bella!'
#
# OUTPUT: 'Enter the lower bound:'
# USER-INT-INPUT: ASSIGN as lower_bound
# OUTPUT: 'Enter the higher bound:'
# USER-INT-INPUT: ASSIGN as higher_bound
# OUTPUT: 'Great, now guess a number between {} and {}'.format(lower_bound,higher_bound)
# 
# USER-INT-INPUT: ASSIGN as user_guess
# ASSIGN: RANDOM-INT using RANDOM LIB as random_number WITH RANGE (lower_bound, higher_bound)
# ASSIGN: random_number to random_number
#
# FOR number in RANGE (random_number):
#   IF user_guess is LESS then random_number:
#       OUTPUT: 'Nope too low.'
#       OUTPUT: 'Guess another number:'
#       USER-INT-INPUT: ASSIGN to user_guess
#   IF user_guess is MORE then random_number:
#       OUTPUT: 'Nope too high.'
#       OUTPUT: 'Guess another number:'
#       USER-INT-INPUT: ASSIGN to user_guess
# ASSIGN: user_guess to random_number
# OUTPUT: 'You did it!'
#
import random
print('Welcome to the Higher/Lower game Bella!')

print('Enter the lower bound:')
lower_bound = int(input())
print('Enter the higher bound:')
higher_bound = int(input())
print('Great, now guess a number between {} and {}'.format(lower_bound,higher_bound))

user_guess = int(input())
random_number = random.randint(lower_bound,higher_bound)
random_number = random_number

for number in range(random_number):
    if user_guess < random_number:
        print('Nope too low')
        print('Guess another number:')
        user_guess = int(input())
    if user_guess > random_number:
        print('Nope too high')
        print('Guess another number:')
        user_guess = int(input())
user_guess = random_number
print('You did it!')