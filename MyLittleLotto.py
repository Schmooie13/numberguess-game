#My Little Lotto v0.1
#This is only my second program...let's see how it goes.

#Print game prompt
print ('# Welcome to My Little Lotto #')
print ()
print ('Your job in this game is guess the correct number(1-10).')
print ('You will have four chances to get the number correct.')
print ('Complete all four rounds and win!')
print ()
#Pull a random number into a variable
import random
random_num = random.randint(1,10)
num_guesses = 4
#Start guessing prompt
while True:
    guess = input('Please enter a number between 1-10: ')

    if int(guess) < 1 or int(guess) > 20:
        print ('Invalid number. Please enter a number between 1-10.')
    elif int(guess) == random_num:
        print ('You have guessed correctly!~ You win!')
        break
    else:
        num_guesses -= 1
        print ('You have failed to guess correctly. You have ' + str(num_guesses) + ' try(s) left.')
        if num_guesses == 0:
            print ('You have no more guesses. Better luck next time')
            break
