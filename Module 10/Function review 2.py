#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program multiplies a number by two.

def printDouble(a):
    #function accepts number from main
    #multiply number by two
    ans = a*2
    #prints equation plus answer
    print("2 *",a,"=",ans)
         

def printEndMessage():
    #This function tells the user it has finished
    print("This program has finished. Goodbye.")


def main():
    num1 = int(input("Please enter yor number "))
    printDouble(num1)
    printEndMessage()

main()

