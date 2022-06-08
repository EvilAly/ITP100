#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Final Project-Part 3 - Prints a list of all the health districts on the VDH
#COVID data.

def main():
    #open the file
    report = open('Covid Data.txt')

    #create VDH District list
    vdh = []

    #read the first line of the file
    discard = report.readline()
     
    for day in report:
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
    print('A total of',(len(vdh)),'Health Districts were found.')

main()

