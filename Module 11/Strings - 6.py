#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program takes a string and prints the number of upper case letters in the string.

#define main
def main():
    userString = input('Please enter a string:')

    #start my counter at zero
    caps = 0
    
    #for each letter in the string (hint: for locations 0 through 1 less than the length of the string)
    for letter in userString:
             
        #if this letter is a capital letter, add one to my counter
        if letter.isupper():
            caps = caps + 1
       
    print('Your string has',caps,'capital letters.')
  
#call main
main()
