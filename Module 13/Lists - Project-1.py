#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Lists-Project-1
#This program looks at a txt tile and creates a table with Sales by Department
#and total sales listed at the bottom.

def main():

    #initializes variables
    gsales = 0
    lsales = 0
    psales = 0
    tsales = 0

    #opens file
    sales = open('inventory.txt')

    #looks at each line in file
    for line in sales:
        #strips spaces and "return" entries
        line = line.strip()

        #creates list from the line
        sList = line.split(',')

        if sList[0] == 'Garden':
            #line is for the garden dept
            #adds sale to appropriate department
            gsales = gsales + float(sList[2])

            #adds sale to total sales
            tsales = tsales + float(sList[2])

        if sList[0] == 'Plumbing':
            #line is for the plumbing dept
            #adds sale to appropriate department
            psales = psales + float(sList[2])

            #adds sale to total sales
            tsales = tsales + float(sList[2])

        if sList[0] == 'Lighting':
            #line is for the lighting dept
            #adds sale to appropriate department
            lsales = lsales + float(sList[2])

            #adds sale to total sales
            tsales = tsales + float(sList[2])

    print('Sales by Department:')
    print('\nPlumbing:  $',round(psales,2))
    print('Lighting:  $',round(lsales,2))
    print('Garden:  $',round(gsales,2))
    print('\nTotal Sales:  $',round(tsales,2))


main()

