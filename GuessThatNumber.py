#Guess That Number! v0.1
#This is only my second program...let's see how it goes.

def main():
    #Print game prompt
    print ('# Welcome to Guess That Number v0.2 #')
    print ('Your job in this game is guess the correct number(1-25).')
    print ('You will have five chances to get the number correct.\n')
    #Pull a random number into a variable
    import random
    random_num = random.randint(1,25)
    num_guesses = 5
    #Start guessing game
    while True:
        guess = input('Please enter a number between 1-25: ')

        if int(guess) < 1 or int(guess) > 25:
            print ('Invalid number. Please enter a number between 1-25.')
        elif int(guess) == random_num:
            print ('You have guessed correctly!~ You win!')
            break
        else:
            num_guesses -= 1
            if num_guesses == 0:
                print ('You have no more guesses. Better luck next time.')
                print ("P.S. The correct number was %s." % random_num)
                break
            else:
                if int(guess) < random_num:
                    print ('You have failed to guess correctly. You have %s try(s) left.' % num_guesses)
                    print ('Your number was less than target number.')
                elif int(guess) > random_num:
                    print ('You have failed to guess correctly. You have %s try(s) left.' % num_guesses)
                    print ('Your number was higher than target number.')

main()
