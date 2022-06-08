#Aubrey Wilcher
#abradford0001@email.vccs.edu

#  "Fun with Files" - Demo for reading from a file and countying occurances of a string

def main():

    #open the file for reading
    myFile = open('demo file data 1.txt')

    #start counter at zero
    counter = 0

    #for each line in the file, read it
    for line in myFile:

        #if "This" is foudn in this line, add 1 to the counter
        if line.find('This') >= 0:   #if "This" is found in this line
            counter = counter + 1

    #print the number of lines containing "This" that were found
    print('Your file had',counter,'lines with the word This')
    
main()
