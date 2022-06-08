#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program finds the square root of a positive integer.

#Loads the built-in math function.
import math

#Defines main
def main():
  
  #Asks user for positive integer
  num = input("Enter a positive integer and I will calculate the square root ")
  
  try:
    #Converts input to an integer.
    number = int(num)
    
    #Determines the square root.
    root = math.sqrt(number)
    
    #Returns the results. 
    print("The square root of ",num,"is ",root)
    
  except:
    #Tells the user to enter a positive integer.
    print("Please enter a positive integer")

#Calls main
main()
