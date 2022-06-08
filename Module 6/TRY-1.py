#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program asks a user for their age and determines if it is an integer.

#Define main
def main():
  
  #Ask user for age
  age = input("Please enter your age ")
  
  try:
    #Verify that an integer was entered.
    AgeAsInt = int(age)

    #Integer was entered.
    print("Valid input")
  
  except:
    #Something other than an integer was entered.
    print("You did not enter an integer for age.")

#Call main  
main()
