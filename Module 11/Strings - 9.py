#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program changes a word into Pig Latin.


#define main
def main():
    word = input('Please neter a word ')

    #looks at first letter of word
    first = word[0]

    if first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U':
        #first letter is a vowel
        #add "HAY" to end
        vowel = word + "HAY"
        print(vowel)
    else:
        #first letter is a consonant
        #move first letter to end & add "AY"
        con = word[1:] + first + "AY"
        print(con)
    
#call main
main()
 
