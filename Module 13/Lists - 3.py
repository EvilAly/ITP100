#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Lists-3 - Asks user for five string values to create a list. Then asks user to
#for a string to find. Gives appropriate response. 

def main():
    #create list
    myList = []

    #start counter at 0
    counter = 0

    while counter < 5:
        #Asks user for a string
        st = input("Enter a string: ")

        #Add string to list
        myList.append(st)

        #Add 1 to counter
        counter = counter + 1

    #asks user for which string they're looking for
    look = input("What are you looking for? ")

    #check list for string
    try:
        check = myList.index(look)
        #word found in list
        print("You found it at index",check)
    
    except:
        #string is not found in the list
        print(look,'was not in your list')
    
main()
