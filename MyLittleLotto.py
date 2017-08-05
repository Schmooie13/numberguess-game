#My Little Lotto v0.1
#This is only my second program...let's see how it goes.

#Print game prompt
print ('# Welcome to My Little Lotto #')
print ()
print ('Your job in this game is to go through six rounds of guessing the')
print ('correct number(1-20). You will have four chances to get the number correct.')
print ('Complete all six rounds and win!')
print ()
#Pull a random number into a variable
import random
random_num = random.randint(1,5)
#Start guessing prompt
while True:
    guess = input('Please enter a number between 1-20: ')
    if int(guess) == random_num:
        guessed_correct = True
        print ('You guessed correctly')
        if guessed_correct == True:
            random_num = random.randint(1,5)
