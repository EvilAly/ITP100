#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program allows the user to play a simple game of 21 versus the computer.

#Loads the random built-in function
import random

def main():

    #Greet the user
    print('Hello player')

    #Deals user their first card
    first = random.randint(1,10)

    #Gives user their first value
    print("Your first card is a {}.".format(first))

    #Deals user their second card
    second = random.randint(1,10)

    #Gives user their second value
    print("Your second card is a {}.".format(second))

    #Asks if user wants to hit
    hit = input("Do you want to hit?")

    #Determines user wants third card, then calculates the user's total
    if hit == "y" or hit == "yes":
        third = random.randint(1,10)
        print("Your third card is a {}.".format(third))
        total = first + second + third
    else:
        total = first + second

    #Informs user of their total.
    print("Your total is {}.".format(total))

    #Assigns random total to dealer
    dealer = random.randint(10,21)

    #Informs user of dealer's total
    print("The dealer has a {}.".format(dealer))

    #Determines winner
    if total > dealer and total <= 21:
        print("Congratulations! You've won!")
    else:
        print("Dealer wins. Please try again.")


main()
