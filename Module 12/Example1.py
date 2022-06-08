#Aubrey Wilcher
#abradford0001@email.vccs.edu

#  "Fun with Files" - Demo for writing to a file

def main():
    # create a file named myFileOut and prepare it to be written to
    myFileOut = open('myfriends.txt','w')
    # ask for a name of a friend
    friend = input('Enter friend name -- type stop to quit ')

    # as long as stop has not been entered
    while friend != 'stop':
        #write the friend's name to the file
        myFileOut.write(friend+'\n')

        #ask user for another name
        friend = input('Enter friend name -- type stop to quit ')

    #close the file
    myFileOut.close()

main()
