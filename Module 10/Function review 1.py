#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program is for a dice game using 6-sided die. The closest player to 9
#without going over wins. Ties go to the player.

import random

#define functions
def rollDice():
    #function returns a random number between 1 and 6
    a = random.randint(1,6)
    print("A",a,"has been rolled.")
    return a

def userWon(t1, t2):
    #function accepts player total and computer total
    #function compares two numbers
    if (t1 >= t2):
        #player has higher number
        if (t1 <= 9):
            #player has gone over
            msg = 'true'
        #player has 9 or less
        else:
            msg = 'false'
    else:
        #computer has higher number
        if (t2 > 9) and (t1 <= 9):
            #computer is over, but player is not
            msg = 'true'
        else:
            #both are over
            msg = 'false'
        
    return msg

def main():
    #each player rolls two dice
    player = rollDice() + rollDice()
    computer = rollDice() + rollDice()
    #ask the player if they want to roll again
    again = int(input("Please enter 1 to roll again. Enter 2 to hold."))
    #roll again if needed and add to player's total
    if again == 1:
        player = player + rollDice()

    #Compares the values to determine if the user won.
    results = userWon(player,computer)
    
    #Print appropriate statements
    if results == 'true':
        print("Congratulations! You have won!")

    else:
        print("I'm sorry. You have lost.")
        
main()
