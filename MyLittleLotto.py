#My Little Lotto v0.1
#This is only my second program...let's see how it goes.

#Print game prompt
print ('# Welcome to My Little Lotto #')
print ()
print ('Your job in this game is to go through six rounds of guessing the')
print ('correct number(1-20). You will have four chances to get the number correct.')
print ('Complete all six rounds and win!')
print ()
#Start guessing prompt
while True:
    guess = input('Please enter a number between 1-20: ')
    if int(guess) < 1 or int(guess) > 20:
        print ('Invalid number - not between 1-20. Try again!')
