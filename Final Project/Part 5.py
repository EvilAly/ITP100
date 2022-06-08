#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project- Part 5 - A menu program that asks the user to make a choice.

def menu():

    #Greets user and gives options
    print('Hello. Please choose one of the following options:')
    print('1. Display all data for a location.')
    print('2. Diplay the date of the greatest increase in deaths for a location.')
    print('3. Display a list of the health districts.')
    print('4. Display the date the number of cases exceeded a given value.')
    print('5. Quit')

    #asks user for their option number
    ans = int(input('Please enter a number: '))

    #returns user's answer to main
    return ans
    
def main():

    #runs the menu function
    opt = menu()

    while opt != 5:
        if opt == 1:
            #user selected option 1
            print('You chose option 1.\n')
            #returns to the menu
            opt = menu()
        
        elif opt == 2:
            #user selected option 2
            print('You chose option 2.\n')
            #returns to the menu
            opt = menu()
        
        elif opt == 3:
            #user selected option 3
            print('You chose option 3.\n')
            #returns to the menu
            opt = menu()
        
        elif opt == 4:
            #user selected option 4
            print('You chose option 4.\n')
            #returns to the menu
            opt = menu()
        
        else:
            #user entered an invalid number
            print('Invalid choice\n')
            #returns to the menu
            opt = menu()

    #user entered quit/option 5
    print('Goodbye.')
           

main()

