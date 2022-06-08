#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program welcomes the user, then asks user for 2 integers. The 2 numbers
#are then multiplied and the results given.

def greeting(name):
    #This function greets the user
    print("Hello",name)

def multiply2nums(a,b):
    #This function multiplies 2 numbers together and returns the results
    prod = a * b
    return prod

def main():
    user = input("Please enter your name ")
    greeting(user)
    try:
        num1 = int(input("please enter an integer "))
        num2 = int(input("please enter another integer "))
        result = multiply2nums(num1,num2)
        print("The product of your two numbers is ",result)
    except:
        print("Error found in input")

main()

