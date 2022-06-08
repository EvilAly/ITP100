#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program is a simple calculator that adds, subtracts, multiplies, and divides two numbers.
#It also returns if there a dividing remainder and the exponential. 

# define userInput
def userInput():

    #ask for first number
    a = input('Enter your first number: ')

    #ask for second number
    b = input('Enter your second number: ')

    return (a,b)

#define add
def add(a,b):

    #adds the two integers
    total = a + b

    #returns total to main
    return total

#define subtract
def subtract(a,b):

    #subtracts the two integers
    diff = a - b

    #returns the difference
    return diff

#define multiply
def multiply(a,b):

    #multiplies the two integers
    x = a * b

    #returns the answer
    return x

#define divide
def divide(a,b):

    #divides the numbers
    quo = a / b

    #returns the quotient
    return quo


#define modulo
def modulo(a,b):

    #determines if there is a remainder
    rem = a % b

    #returns the remainder
    return rem

#define exponent
def exponent(a,b):

    #Multiples 1st value by 2nd power
    exp = a ** b

    #returns the answer
    return exp

#define output
def userOutput(a,b,c,d,e,f,g,h):

    #Gives user the addition results
    print(a,' + ',b,' = ', c)

    #Gives user the subtraction results
    print(a,' - ',b,' = ', d)

    #Gives user the multiplication results
    print(a,' * ',b,' = ', e)

    #Gives user the division results
    print(a,' / ',b,' = ', f)

    #Gives user the modulo results
    print(a,' % ',b,' = ', g)

    #Gives user the exponent results
    print(a,' ** ',b,' = ', h)

#define main
def main():

    (first,second) = userInput()

    if second != '0':
        try:
            #try to convert to integers
            fst = float(first)
            snd = float(second)

            #run numbers through add
            summary = add(fst,snd)

            #run numbers through subtract
            difference = subtract(fst,snd)

            #run numbers through multiplication
            mult = multiply(fst,snd)

            #run numbers through division
            div = divide(fst,snd)

            #run numbers through modulo
            mod = modulo(fst,snd)

            #run numbers through exponent
            expon = exponent(fst,snd)

            #Returns results
            userOutput(fst,snd,summary,difference,mult,div,mod,expon)

        except:
            #integer not entered
            print('Please enter a valid integer.')

    else:
        print('You cannot divide by 0.')

   
main()
    



