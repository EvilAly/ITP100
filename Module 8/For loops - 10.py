#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program prints a triangle of stars with a base of a user given number.

#define main
def main():

    #gets max number of stars from user
    star = int(input('How wide would you like your triangle? '))

    #build the triangle
    for s in range (0,star+1):
        print((star-s)*' ',s*'*')


#calls main
main()


