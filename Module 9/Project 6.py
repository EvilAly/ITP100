#Program works, but will occassionally tell you a number is not an integer.
#You can re-enter the number and it continues fine.

#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program creates a guessing game. A random number between 1 and 100 will be
#generated, which the user will have to try to guess. The program will tell the
#user if their guess is too high, too low, or correct and the number of guesses
#to guess the number.



#load random
import random

#Define printInstructions
def printInstructions():

    #Tells user the instructions
    print("A random number from 1 to 100 will be generated. You will enter numbers")
    print("until you have guessed correctly. A tally of the number of guesses will")
    print("be kept.")

#Define printResults
def printResults(a):

    #Congratulates winner and gives total number of attempts
    print("Congratulations! You've guessed correctly!")
    print("It took you",a,"attempts")
    

#Define game
def game():
    
    #Asks user for their guess
    g = input("Please enter your guess ")
    return g

#Define main
def main():

    #Tells user how to play
    printInstructions()

    #create random number
    ans = random.randint(1,100)

    #Set count to 0
    cnt = 0

    #Ask user to guess the number
    guess = game()
    
    #While guess is incorrect
    while guess != ans:

        #Verify guess in an integer
        try:
            guess = int(guess)

            #Guess is too high
            if guess > ans:
                print("Your guess is too high.")
                cnt = cnt + 1
                guess = game()

            #Guess is too low
            if guess < ans:
                print("Your guess is too low.")
                cnt = cnt + 1
                guess = game()

            #Guess is correct
            else:
                cnt = cnt + 1
                printResults(cnt)

        #Guess was not an integer
        except:
            print("You did not enter an integer.")
            guess = game()


main()
