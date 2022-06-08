#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program takes a string and tells the user if it is or is not a palindrome.

#define main
def main():
    myWord = input("Please enter a string")

    #make the string all uppercase
    myWord = myWord.upper()

    #reverse the input string
    revWord = myWord[::-1]

    if myWord == revWord:
        print('IS A PALINDROME')
    else:
        print('IS NOT A PALINDROME')
    
  
#call main
main()
