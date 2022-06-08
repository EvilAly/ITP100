#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program is for a dice game. Three 8-sided dice are rolled and the face values totaled. A roll of 10, 15, or 20 wins the game. 

#Imports the random built-in function.
import random

def main():
  
  #Asks the user if they would like to play
  ans = input("Would you like to play a game?")
  
  #If player answers yes, the three dice are rolled at random.
  if ans == "y" or ans == "yes":
    first = random.randint(1,8)
    second = random.randint(1,8)
    third = random.randint(1,8)
    
    #Add three rolls together.
    total = first + second + third
    
    #Gives user their rolls and their total.
    print("You rolled a {},".format(first),"a {},".format(second),"and a",third,"for a total of {}.".format(total))
    
    #Determines if the user won or lost, and prints the results.
    if total == 10 or total == 15 or total == 20:
        #Player wins
      print("CONGRATULATIONS!!! You won!")
    else:
        #player lost
      print("You have lost. Please play again.")
      
  #If user does not want to play, offer to play later.
  else:
    print("Maybe another time.")
  
  
  
  
main()
