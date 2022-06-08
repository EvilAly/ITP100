#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program asks the user to enter numbers. It will keep track of the smallest
#number until the user equals '0' to abort the program.

#THIS PROGRAM WORKS WITH ALL EXAMPLE CASES

def main():

    #Ask user for first number
    num =int(input('Please enter a number '))

    #Number is zero
    if num == 0:
        print("Program aborted")

    #otherwise set smallest number
    else:
        small = num

        #As long as entered number isn't zero
        while num != 0:

            #Ask for a number
            num = int(input('Please enter a number '))

            #Compare number to smallest and set smallest = to number if needed
            if num < small and num != 0:
                small = num
    

        #Print smallest number
        print('Your smallest number was',small)
        

main()
