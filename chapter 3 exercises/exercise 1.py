# Exercise,Number Guessing Game
# make a variable,like winning_number and assign any number to it.
# Ask user to guess a number
# if user guessed correct number then print "You Are Winner !!!"
# if user didn't guessed correctly then:
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"

#google "how to generate random numer in python" to generate random
#winning number

winning_number=[6,7,8,9]
guessed_num=int(input())
if guessed_num == winning_number:
    print("You Are Winner")
    if guessed_num < winning_number:
        print("too low")
    else:
        print("too high")


        
