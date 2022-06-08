#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Files - Program 1 - writes a user's integers to a file

def entry():
    #asks user for a number
    ans = input('Please enter a number -- enter a negative to stop ')

    #attempt conversion to integer
    con = convert(ans)

    #returns input
    return con

def convert(a):
    
    try:
        #tries to convert input to an integer
        inp = int(a)
        #returns integer
        return inp

    except:
        #user did not enter an integer
        print('You did not enter a valid integer.')
        #asks for another input
        again = entry()
        #returns new input
        return again       
                                
def main():

    #opens file and prepares to write
    numFile = open('numbers.txt','w')

    #get first number and tries to convert
    num = entry()

    #a positive integer has been entered
    while num > 0:

        #adds string and end of line to write to file
        numFile.write(str(num)+'\n')

        #get next number and attempt conversion
        num = entry()

    #close the file
    numFile.close()   
        

main()
