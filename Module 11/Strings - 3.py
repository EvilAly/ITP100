#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program prints the word Certainly or Why Not depending on the input from
#the user.

#define main
def main():
    answer = input('Please enter yes or no')

    #formats the answer to all uppercase
    ans = answer.upper()

    if ans == "YES":
        #user entered YES
        print("CERTAINLY")
    else:
        print("WHY NOT?")
  
#call main
main()
