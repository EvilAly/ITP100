#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Files - Reading from files - reads the numbers from a file and displays the sum
#minimum, maximum, average, and the number of values in the file.

def main():

    #opens file for reading
    numFile = open('numbers.txt')

    #sets required variables to zero
    #sets minimum to none
    add = 0
    maximum = 0
    minimum = 'none'
    counter = 0
    
    
    #for each line in the file
    for line in numFile:

        #Converts number to integers
        num = int(line.rstrip())

        #adds number
        add = add + num

        #determines maximum
        if maximum < num:
            maximum = num
        #determines minimum
        elif minimum == 'none' or minimum > num:
            minimum = num

        #add one to counter
        counter = counter + 1

    #determines average
    average = float(add/counter)

    #rounds average
    average = round(average,2)

    print('The following are the results for the file numbers.txt.')
    print('The total is',add)
    print('The maximum is',maximum)
    print('The minimum is',minimum)
    print('There are',counter,'numbers in the file.')
    print('The average of these numbers are',average)
            

main()
