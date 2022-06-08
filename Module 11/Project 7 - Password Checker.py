#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program tells the user if a password is valid or invalid based on a specific
#set of criteria.

#define main
def main():
    #asks user for the password
    pword = input('Please enter a password')

    #assign variables
    cap = 0
    low = 0
    num = 0
    
    #check password parameters
    if len(pword) >= 8:
        #password is at least 8 characters
        for letter in pword:
            if letter.isupper():
                #password has an uppercase
                cap = 1    
            elif letter.islower():
                #password has a lowercase
                low = 1
            elif letter.isdigit():
                #password has a number
                num = 1
        if pword[0].isalpha():
            #first character is a letter
            print("INVALID")
        else:
            if pword.isalnum():
                #password is missing special character
                print("INVALID")
            elif cap > 0 and low > 0 and num > 0:
                #all parameters are met
                print("VALID")
            else:
                #password does not start with a character, but is missing a capital, lower, or number
                print("INVALID")
    else:
        #password is not at least 8 characters
        print("INVALID")
  
  
#call main
main()
