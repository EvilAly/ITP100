#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program asks the user for a string, and then a character. It replaces the
#given character with an underscore in their string.


#define main
def main():
    userString = input('Enter a string:')
    userChar = input('Enter a character:')

    #Replaces user string with new string with replaced character(s)
    userString = userString.replace(userChar,"_")


    print(userString)
  
#call main
main()
