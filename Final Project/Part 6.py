#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project- Part 6 - This program gives the user a menu to select how to
#process and view the information they require. After each step, the user is
#prompted to select another option until the program is exited.

def locationData(fn,loc):

    #read and discard header
    header = fn.readline()

    #set counter
    count = 0

    for date in fn:
        #strip blanks
        date = date.rstrip()

        #convert line to a list
        day = date.split(',')

        if day[2] == loc:
            #area is listed on the line
            if count == 0:
                #first time location is found
                #print header information
                print('Locality: ',loc)
                print("Date          Cases     Hosp    Deaths")

            #print data for that day
            print(day[0],'\t',day[4],'\t',day[5],'\t',day[6])

            #area was found, so add to counter
            count = count + 1

    if count == 0:
        #locality was not found
        print(loc,'was not found in the file.\n')


def increaseDate(fn,loc):

    #set variables to zero
    prev = 0
    high = 0
    period = 0
    count = 0

    for date in fn:
        #strip blanks
        date = date.rstrip()

        #create list
        day = date.split(',')

        if loc == day[2]:
            #line is for user's area
            #look at number of cases
            case = day[4]

            #add to count
            count = count + 1

            if prev == 0:
                #set first day to prev
                prev = case

            else:
                #subtract two days
                diff = int(case) - int(prev)

                if diff > high:
                    #difference is highest number
                    #set new high
                    high = diff
                    #Set new date
                    period = day[0]                

                #set today to prev
                prev = case

    if count == 0:
        #area is not in file
        print('No data was found for',loc,'\n')

    else:
        #prints results
        print(period,'had the highest with',high,'new cases.\n')


def districtList(fn):

    #create VDH District list
    vdh = []

    #read the first line of the file
    discard = fn.readline()
     
    for day in fn:
        #strip any blanks at beginning or end
        day = day.rstrip()

        #convert to list
        result = day.split(',')

        #finds district
        dist = result[3]

        if dist not in vdh:
            #adds new district to list
            vdh.append(dist)

    for entry in vdh:
        #prints each district in the list
        print(entry)

    #prints total number of districts found
    print('A total of',(len(vdh)),'Health Districts were found.\n')


def exceeding(fn,loc,n):

    #toss header line
    header = fn.readline()

    #create variables
    count = 0
    date = 0
    cases = 0

    for data in fn:
        #strip blanks
        data = data.rstrip()

        #create list
        day = data.split(',')

        if loc == day[2]:
            #line matches locality
            #add to count
            count = count + 1

            if n < int(day[4]) and date == 0 and cases == 0:
                #number of cases is higher than target
                date = day[0]
                cases = day[4]

    if count == 0:
        #area is not in the file
        print('No data was found for',loc,'\n')

    elif cases == 0:
        #area is in file, but did not exceed number of cases
        print(loc,'has not passed',n,'number of cases.\n')

    else:
        #prints results
        print(loc,'passed',n,'cases on',date,'with',cases,'number of cases.\n')
                

def displayMenu():

    #Greets user and gives options
    print('\n')
    print('Hello. Please choose one of the following options:')
    print('1. Display all data for a location.')
    print('2. Diplay the date of the greatest increase in cases for a location.')
    print('3. Display a list of the health districts.')
    print('4. Display the date the number of cases exceeded a given value.')
    print('5. Quit')

    #asks user for their option number
    ans = int(input('Please enter a number: '))

    #adds space between menu and data
    print('\n')

    #returns user's answer to main
    return ans


def main():

    #initialize opt variable
    opt = 0

    while opt != 5:

        #open file
        report = open('covid data.txt')
        
        #run menu file
        opt = displayMenu()
        
        if opt == 1:
            #user selected option 1
            #asks user for the location
            area = input("Which city or county would you like to view? ").title()

            #calls function with file and locality
            locationData(report,area)
                    
        elif opt == 2:
            #user selected option 2
            #asks user for location and formats
            area = input("Which city or county would you like to view? ").title()

            #calls function with file and locality
            increaseDate(report,area)
                   
        elif opt == 3:
            #user selected option 3
            #calls function with file
            districtList(report)

        elif opt == 4:
            #user selected option 4
            #get locality from user
            area = input('Please enter a location: ').title()

            #get number to search
            target = int(input('Please enter the number of cases: '))

            #calls function with file, locality, and target number
            exceeding(report,area,target)            
        
        elif opt != 5:
            #user entered an invalid number
            print('You have entered an invalid option. Please select again.\n')
            
            

    #user entered quit/option 5
    print('Goodbye.')


main()
