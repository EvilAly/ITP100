#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project-Part 1 - Asks for name of city/county and prints the COVID-19
#data for that locality.

def main():

    #open file
    report = open('covid data.txt')

    #read file so area can be checked for
    data = report.read()

    #ask user for area
    area = input("What city or county would you like to view? ")

    #formats input to match formating in file
    area = area.title()

    #reopen file to be read as lines
    report = open('covid data.txt')

    #check file for area
    if area in data:
        #area is located in the file
        #print heading info
        print('Covid Data for',area)
        print('Date','      ','Cases',' ','Hospitalizations',' ','Deaths')        

        for date in report:
            #strip blanks
            date = date.rstrip()

            #convert line to list
            day = date.split(',')

            if day[2] == area:
                #print results for that day
                print(day[0],'  ',day[4],'     ',day[5],'               ',day[6])

    else:
        #area not in covid data
        print('No data was found for',area)

main()
