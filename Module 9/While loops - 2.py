#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program adds numbers entered by a user until they enter a negative number,
#then returns the result.

#THIS PROGRAM WORKS FOR ALL SAMPLE CASES

def main():

    #sets total to 0
    total = 0

    #Asks user for an integer, and advises how to end
    num = int(input('Please enter an integer -- enter a negative to stop '))

    #As long as the entered number is not negative
    while num >= 0:
    
        #Adds new number to the total
        total = total + num

        #Asks user for a new integer
        num = int(input('Please enter an integer -- enter a negative to stop '))

    #Returns the user's total
    print('Your total is ',total)    

main()
