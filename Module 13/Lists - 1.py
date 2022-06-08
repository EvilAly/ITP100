#Aubrey Wilcher
#abradford0001@email.vccs.edu

# Lists-1 - Asks user for sentence, then print the words in reverse order.

def main():
    sentence = input("Please enter a sentence ")

    #converts sentence into a list
    words = sentence.split(' ')

    #reverses the list
    words.reverse()

    #prints the reversed list
    print(words)

main()
