#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project- Part 4 - Asks the user for a locality & a number. Returns the
#date the locality exceeded that number of cases.

    
def main():

    #opens the file
    report = open('Covid Data.txt')

    #toss header line
    header = report.readline()

    #get locality from user
    area = input('Please enter a location: ').title()

    #get number to search
    target = int(input('Please enter the number of cases: '))

    #create variables
    count = 0
    date = 0
    cases = 0

    for data in report:
        #strip blanks
        data = data.rstrip()

        #create list
        day = data.split(',')

        if area == day[2]:
            #line matches locality
            #add to count
            count = count + 1

            if target < int(day[4]) and date == 0 and cases == 0:
                #number of cases is higher than target
                date = day[0]
                cases = day[4]

    if count == 0:
        #area is not in the file
        print('No data was found for',area)

    else:
        #prints results
        print(area,'passed',target,'cases on',date,'with',cases,'number of cases.')
                

main()

