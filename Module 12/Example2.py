#Aubrey Wilcher
#abradford0001@email.vccs.edu

#  "Fun with Files" - Demo for writing numbers to a file

def main():
    # open file and prepare for writing to it
    myNumberFile = open('mynumbers.txt','w')

    #get number from the user
    num = float(input('Enter decimal number -- type 0 to stop '))

    #as long as zero hasn't been entered
    while num != 0.0:

        #convert num to string and adds end of line to write to file
        myNumberFile.write(str(num)+'\n')

        #get next number
        num = float(input('Enter decimal number -- type 0 '))

    #close the file
    myNumberFile.close()
    
main()
