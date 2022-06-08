#Aubrey Wilcher
#abradford0001@email.vccs.edu

#This program gathers a user's name, vacation destination, and the distance to determine the best possible mode
#of transportation and the time it will take to arrive.

def main():
  #Asks user for name, desitnation, and distance
  name = input("What's your name? ")
  destination = input("Where would you like to vacation? ")
  miles = int(input("How many miles away is that? "))
  
  #Greets user
  print("Hello",name)
  
  #States destination
  print ("You want to vacation at",destination)
  
  #Calculates best mode of transportation
  if miles >= 1000:
    mode = 'fly'
  elif miles < 50:
    mode = 'walk'
  else:
    mode = 'drive'
    
  #Calculates travel time
  if mode == 'fly':
    travel = (miles / 550)
  elif mode == 'walk':
    travel = (miles / 3)
  else:
    travel = (miles / 50)

  #Round travel time to 2 digits
  time = round(travel,2)
  
  #Gives user the best mode of transportation and the time it will take to arrive.  
  print("for this trip you will {}.".format(mode),"The trip will take you about",time,"hours.")
  

main()
