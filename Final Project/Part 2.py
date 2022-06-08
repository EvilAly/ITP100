#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project-Part 2 - Asks for name of city/county and prints the date and
#number of cases for the highest day.

def main():

    #open file
    report = open('covid data.txt')

    #ask user for area
    area = input("Which city or county would you like to view? ")

    #format area
    area = area.title()

    #set variables to zero
    prev = 0
    high = 0
    period = 0
    count = 0

    for date in report:
        #strip blanks
        date = date.rstrip()

        #create list
        day = date.split(',')

        if area == day[2]:
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
        print('No data was found for',area)

    else:
        #prints results
        print(period,'had the highest with',high,'new cases.')


main()
