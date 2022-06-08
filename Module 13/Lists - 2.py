#Aubrey Wilcher
#abradford0001@email.vccs.edu

# Lists-2 - Asks user for sentence, prints the 5th letter of the 4th word. 

def main():
    sentence = input("Please enter a sentence ")

    #turns sentence into a list
    sent = sentence.split(" ")

    
    try:
        #There is a 4th word
        four = sent[3]

        try:
            #There is a 5th letter in the 4th word
            letter = four[4]

            #prints the 5th letter
            print(letter)

        except:
            #The 4th word does not have at least 5 letters
            print("The 4th word was too short")

        
    except:
        #There is not a 4th word.
        print("Sentence was too short")

    

    

main()
