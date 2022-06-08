#Aubrey Wilcher
#abradford0001@email.vccs.edu

# This program asks the user for a number, find the sum of the numbers from 1
# to (and including) their number, then gives user the total sum.

# define main
def main():

    # asks user for a number
    num = input('What is your number? ')

    # set sum = 0
    sum = 0

    try:
        # convert to integer
        last = int(num)

        # use a for loop to count from 1 to 100
        for a in range (1,last+1):

            # add 'this' number to sum
            sum = sum + a

        # outside the loop, print the sum
        print('The sum of the numbers from 1 to',last,'is',sum)

    except:

        # user did not enter an integer
        print('Please enter a whole number.')

     

# calls main
main()



