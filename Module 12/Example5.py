#Aubrey Wilcher
#abradford0001@email.vccs.edu

#  "Fun with Files" - Demo for reading numbers from a file and find the sum

def main():

    #open the file for reading
    myFileIn = open('mynumbers.txt')

    #start sum to 0
    sum = 0

    #for each line in the file
    for line in myFileIn:

        #convert the input string to a float number and strip right end
        num = float(line.rstrip('\n'))

        #print the number
        print(num)

        #add this number to the sum
        sum = sum + num

    #print the total
    print('Grand total was ',sum)
    
main()
