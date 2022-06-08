#Aubrey Wilcher
#abradford0001@email.vccs.edu

#Lists-5 - Prints each item in a given list, and shows the index of each item as well. 

def main():

    #This is a list. We know that because it's in brackets:
    myList = ['Sledgehammer','Rocket Launcher','Nail Gun','Butterfly Net']

    #prints each index number and word
    for tool in myList:
        print("index",myList.index(tool),tool)

main()
