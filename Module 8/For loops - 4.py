#Aubrey Wilcher
#abradford0001@email.vccs.edu

# This program asks the user for a number and then prints "Hello" that many times.

# define main
def main():

    # gets number from user
    num = input('What is your number? ')

    # tries to convert to int
    try:
        time = int(num)

        # loop to print hello for requested number
        for h in range (1, time +1):
            print("Hello")
        
    # user did not enter a valid number
    except:
        print('You did not enter an integer.')

# calls main
main()



