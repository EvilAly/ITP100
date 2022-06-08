#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program prints a sideways triangle, with a user defined maximum height.

#This program works for all 5 requested test values.

#define goingUp
def goingUp(a):

    #build the top (increasing) half of the triangle
    for t in range (1,a+1):
        print(t*'*')

#define goingDown
def goingDown(a):

    #build the lower (decreasing) half of the triangle
    for s in range (a-1,0,-1):
        print((s)*'*')


#define main
def main():

    #gets max number of stars from user
    height = input('How tall would you like your triangle? ')

    #initialize count
    count = 0

    try:

        #user gave positive integer.
        star = int(height)

        if star > 0:
            #user entered positive integer
            #call goingUp
            goingUp(star)

            #call goingDown
            goingDown(star)

        else:
            #user entered 0 or a negative integer
            print('Please use a positive integer.')
        
    except:
        #user did not give an integer
        print('Please use an integer.')

#calls main
main()


