#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program takes a user's city and state, and returns the information in
#sentence form.

#define main
def main():
    # ask user for their city and state
    userInput = input("Please enter your city and state in the form of city,state")

    #determine where the comma is
    com = userInput.find(",")

    #prints statements
    print("You live in the state of",userInput[com+1:])
    print("Your city is",userInput[:com])
    
#call main
main()
