#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program takes a string given by a user and returns it to them in reverse.

#define main
def main():
    origString = input('Please enter a string')

    #assign value to revString
    revString = ' '

    #reverses characters
    for char in origString:
        revString = char + revString
          
    print(origString," printed backwards is ",revString)
   
#call main
main()
