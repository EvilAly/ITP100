#Aubrey Wilcher
#abradford0001@email.vccs.edu

#  "Fun with Files" - Demo for reading from a file and showing contents on screen

def main():

    #open the file for reading
    myFile = open('demo file data 1.txt')

    #for each line in the file
    for eachLine in myFile:
        print(eachLine.rstrip('\n'))
    
main()
